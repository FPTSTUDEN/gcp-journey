---
id: manage-kubernetes-in-google-cloud-challenge-lab
title: "Manage Kubernetes in Google Cloud: Challenge Lab"
source_url: ""
completed_on: ""
record_status: draft # draft | reviewed
progress_status: majority-completed # not-started | in-progress | partial | majority-completed | completed | not-verified
evidence_summary: observed # observed | reported | inferred | unverified
tags:
  topic:
    - containers
    - observability
    - deployment-automation
  skill:
    - configuration
    - deployment
    - monitoring
    - troubleshooting
    - debugging
  service:
    - gke
    - cloud-monitoring
    - cloud-logging
  context:
    - cluster-management
    - incident-response
---

# Summary
As part of the sandbox environment, your developers have created an Artifact Registry repository named demo-repo that has some code with a basic example application that you will deploy onto a cluster.

Note: This image created in the repo is a containerized version of the code you will be downloading from the spls/gsp510/hello-app bucket later in the lab.
Your tasks will include the following:

Creating a GKE cluster based on a set of configurations provided.
Enabling Managed Prometheus on the cluster for metrics monitoring.
Deploying a Kubernetes manifest onto the cluster, and debugging the errors.
Creating a logs-based metric and alerting policy for the errors on the Kubernetes cluster.
Fixing the manifest errors, containerizing your application code and pushing it to Artifact Registry using Docker.
Exposing a service for your application on the cluster and verifying your updates.

## Progress conclusion
The lab is recorded as **majority-completed**. Observed evidence shows that the cluster was created and verified, Managed Prometheus was enabled, a namespace and monitoring resources were configured, an invalid Kubernetes image was diagnosed through pod and log evidence, a logs-based metric and alert policy were created, and the corrected `helloweb` Deployment rolled out successfully. The updated Go application also passed a local compile check. The learner reports completing the majority of the lab but running out of time before pushing the updated container image. Containerizing and pushing the changed application, exposing the final service, and endpoint verification remain unverified and should not be inferred as complete.

## Evidence collected
- `command-history.md`: sanitized command/output history documenting GKE creation and configuration, Managed Prometheus, namespace setup, Prometheus PodMonitoring, failed and corrected `helloweb` Deployment, warning-log inspection, log-based metric, alert policy, rollout success, and Go compile check.
- Workspace files: monitoring manifests and the corrected `helloweb` deployment manifest are present; the application source reports version `2.0.0`.
- User report: most of the lab was completed, but time expired before pushing the updated changes.
- Project IDs, account identifiers, cluster/resource names, generated IDs, URLs, bucket paths, pod names, and other lab-generated values remain redacted in the history.

## Takeaway
The strongest demonstrated outcome is an end-to-end troubleshooting and observability loop: deploy a deliberately invalid workload, inspect Kubernetes and Cloud Logging evidence, create monitoring automation, correct the manifest, and verify a successful rollout. The unfinished image-publishing and service-exposure steps are the boundary of the recorded progress.

## Questions or gaps
- Whether the updated Go application was ever containerized or pushed to Artifact Registry is unverified.
- Whether the application service was exposed and its endpoint tested is unverified.

## My decision / correction
Accepted the learner’s correction that the lab was substantially completed but unfinished at the image-push stage. Set the record to `majority-completed`; did not mark the lab completed or claim success for the remaining deployment steps. Recommended evidence ranks: `applied` for GKE, deployment, monitoring, and troubleshooting tags; `integrated` for the troubleshooting/observability workflow; `exposure` for any concepts only introduced by the unfinished final steps.
