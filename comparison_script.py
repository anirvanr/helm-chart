import sys
import os
import ruamel.yaml

def flatten_dict(data, parent_key='', sep='.'):
    items = []
    for key, value in data.items():
        new_key = f"{parent_key}{sep}{key}" if parent_key else key
        if isinstance(value, dict):
            items.extend(flatten_dict(value, new_key, sep=sep).items())
        elif isinstance(value, list):
            for index, item in enumerate(value):
                if isinstance(item, dict):
                    sub_items = flatten_dict(item, new_key + f'[{index}]', sep=sep)
                    items.extend(sub_items.items())
        else:
            items.append((new_key, value))
    return dict(items)

def flatten_yaml(yaml_file):
    # Load the YAML file
    yaml = ruamel.yaml.YAML(typ='safe')
    with open(yaml_file, 'r') as file:
        data = yaml.load(file)

    # Flatten the YAML data
    flat_data = flatten_dict(data)

    # Output only the keys
    keys = list(flat_data.keys())
    return keys

if __name__ == '__main__':
    script_name = os.path.basename(sys.argv[0])
    if len(sys.argv) < 2:
        print("""
The script performs a comparison between the data in the values.yaml file and the content of the README.md file.
It prints the keys from values.yaml and indicates their presence in the README.md file. 
If a key is found in the README.md file, it is displayed in green color, indicating that it is present. 
If a key is not found in the README.md file, it is displayed in red color, indicating that it is not found.
        """)
        print(f"Usage: python {script_name} <path/of/chart/dir>")
        sys.exit(1)

    directory_path = sys.argv[1]
    chart_name = os.path.basename(directory_path)

    yaml_file = os.path.join(directory_path, "values.yaml")

    if not os.path.exists(yaml_file):
        print(f"values.yaml file not found in directory: {directory_path}")
        sys.exit(1)

    # Color text
    RED_COLOR = '\033[1;31m'
    GREEN_COLOR = '\033[92m'
    RESET_COLOR = '\033[0m'
    
    banner_width = len(chart_name) + 50 # Adjust as needed
    
    # Print the chart name as a banner
    banner = f"""
{'=' * banner_width}
    {chart_name.center(banner_width)}
{'=' * banner_width}"""
    print(banner)

    keys = flatten_yaml(yaml_file)

    readme_file = os.path.join(directory_path, "README.md")
    if os.path.exists(readme_file):
        with open(readme_file, 'r') as file:
            readme_content = file.read()
            for key in keys:
                if key in readme_content:
                    print(f"{GREEN_COLOR}{key}{RESET_COLOR}")
                else:
                    print(f"{RED_COLOR}{key}{RESET_COLOR}")
    else:
        print(f"README.md file not found in directory: {directory_path}")
