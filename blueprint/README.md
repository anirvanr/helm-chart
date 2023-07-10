
![Version: 0.1.0](https://img.shields.io/badge/Version-0.1.0-informational?style=flat-square) ![Type: application](https://img.shields.io/badge/Type-application-informational?style=flat-square) ![AppVersion: 1.0.0](https://img.shields.io/badge/AppVersion-1.0.0-informational?style=flat-square)

# Chart Name

Short description of the chart.

## Introduction

This Helm chart deploys a [blueprint] on a [Kubernetes](https://kubernetes.io/) cluster using the [Helm](https://helm.sh/) package manager.

## Prerequisites

- Kubernetes cluster
- Helm 3.x.x

## Installation


# Configurable Parameters

The following table lists the configurable parameters of the Helm chart and their default values.

| Parameter                                    | Description                                                                   | Default Value         |
| -------------------------------------------- | ----------------------------------------------------------------------------- | --------------------- |
| `replicaCount`                               | Number of replicas for the deployment                                         | `1`                   |
| `image.repository`                           | Image repository                                                              | `nginx`               |
| `image.pullPolicy`                           | Image pull policy                                                             | `IfNotPresent`        |
| `image.tag`                                  | Image tag (overrides chart appVersion)                                        | `""`                  |
| `imagePullSecrets`                           | List of image pull secrets to use                                             | `[]`                  |
| `nameOverride`                               | Override the name of the chart                                                | `""`                  |
| `fullnameOverride`                           | Override the full name of the chart                                           | `""`                  |
| `serviceAccount.create`                      | Specifies whether a service account should be created                         | `true`                |
| `serviceAccount.annotations`                 | Annotations to add to the service account                                     | `{}`                  |
| `serviceAccount.name`                        | The name of the service account to use                                        | `""`                  |
| `podAnnotations`                             | Annotations to add to the pod                                                 | `{}`                  |
| `podSecurityContext`                         | Security context for the pod                                                  | `{}`                  |
| `containerSecurityContext`                   | Security context for the container                                            | `{}`                  |
| `service.type`                               | Service type (ClusterIP, NodePort, LoadBalancer)                              | `ClusterIP`           |
| `service.externalTrafficPolicy`              | External traffic policy for the service                                       | `""`                  |
| `service.port`                               | Service port                                                                  | `80`                  |
| `service.targetPort`                         | Target port of the service                                                    | `8080`                |
| `service.loadBalancerIP`                     | Load balancer IP for the Service (optional, cloud specific)                   | `""`                  |
| `service.loadBalancerSourceRanges`           | Addresses that are allowed when service is LoadBalancer                       | `[]`                  |
| `service.annotations`                        | Annotations to add to the service                                             | `{}`                  |
| `ingress.enabled`                            | Set to true to enable ingress record generation                               | `false`               |
| `ingress.className`                          | IngressClass that will be be used to implement the Ingress (Kubernetes 1.18+) | `""`                  |
| `ingress.annotations`                        | Annotations to add to the ingress resource                                    | `{}`                  |
| `ingress.hosts`                              | Ingress accepted hostnames                                                    | `chart-example.local` |
| `ingress.annotations`                        | Ingress annotations                                                           | `{}`                  |
| `ingress.path`                               | Ingress path                                                                  | `[/]`                 |
| `ingress.tls`                                | TLS configuration for the ingress                                             | `[]`                  |
| `resources`                                  | Resource requests and limits for the container                                | `{}`                  |
| `livenessProbe.enabled`                      | Set to true to enable liveness probe                                          | `false`               |
| `livenessProbe.path`                         | Liveness probe path                                                           | `"/"`                 |
| `livenessProbe.initialDelaySeconds`          | Number of seconds to wait before starting the probe                           | `30`                  |
| `livenessProbe.periodSeconds`                | Number of seconds between probe checks                                        | `10`                  |
| `livenessProbe.timeoutSeconds`               | Number of seconds after which the probe times out                             | `5`                   |
| `livenessProbe.failureThreshold`             | Number of consecutive failures required to mark the container as unhealthy    | `3`                   |
| `readinessProbe.enabled`                     | Set to true to enable readiness probe                                         | `false`               |
| `readinessProbe.path`                        | Readiness probe path                                                          | `"/"`                 |
| `readinessProbe.initialDelaySeconds`         | Number of seconds to wait before starting the probe                           | `10`                  |
| `readinessProbe.periodSeconds`               | Number of seconds between probe checks                                        | `5`                   |
| `readinessProbe.timeoutSeconds`              | Number of seconds after which the probe times out                             | `3`                   |
| `readinessProbe.successThreshold`            | Number of consecutive successes required to mark the container as healthy     | `1`                   |
| `readinessProbe.failureThreshold`            | Number of consecutive failures required to mark the container as unhealthy    | `3`                   |
| `autoscaling.enabled`                        | Set to true to enable horizontal pod autoscaling                              | `false`               |
| `autoscaling.minReplicas`                    | Minimum number of replicas                                                    | `1`                   |
| `autoscaling.maxReplicas`                    | Maximum number of replicas                                                    | `100`                 |
| `autoscaling.targetCPUUtilizationPercentage` | Target CPU utilization percentage                                             | `80`                  |
| `pdb.enabled`                                | Set to true to enable PodDisruptionBudget                                     | `false`               |
| `pdb.minAvailable`                           | Minimum number of pods that must be available during disruptions              | `1`                   |
| `pdb.maxUnavailable`                         | Maximum number of pods that can be unavailable during disruptions             | `""`                  |
| `nodeSelector`                               | Node selector for pod assignment                                              | `{}`                  |
| `tolerations`                                | Tolerations for pod assignment                                                | `[]`                  |
| `affinity`                                   | Affinity rules for pod assignment                                             | `{}`                  |
