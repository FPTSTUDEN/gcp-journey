# Command history

Append commands and their relevant outputs here. Redact secrets before saving.

**Command history and output**

1. Checked the active project and account:
```powershell
gcloud config get-value project
gcloud auth list --filter=status:ACTIVE --format="value(account)"
```
```text
[REDACTED_PROJECT_ID]
[REDACTED_ACCOUNT]
```

2. Checked whether the cluster already existed:
```powershell
gcloud container clusters describe [REDACTED_CLUSTER_NAME] --zone us-west1-b --project [REDACTED_PROJECT_ID] --format="yaml(name,location,status,releaseChannel,autoscaling,currentNodeCount,currentMasterVersion)"
```
```text
ERROR: ... code=404 ... No cluster named '[REDACTED_CLUSTER_NAME]' in [REDACTED_PROJECT_ID].
```

3. Created the cluster:
```powershell
gcloud container clusters create [REDACTED_CLUSTER_NAME] --project [REDACTED_PROJECT_ID] --zone us-west1-b --release-channel regular --num-nodes 3 --enable-autoscaling --min-nodes 2 --max-nodes 6
```
```text
Creating cluster [REDACTED_CLUSTER_NAME] in us-west1-b...done.
Created [https://[REDACTED_API_URL]].

CRITICAL: ACTION REQUIRED: gke-gcloud-auth-plugin ... was not found or is not executable.
kubeconfig entry generated for [REDACTED_CLUSTER_NAME].

NAME              LOCATION    MASTER_VERSION      NODE_VERSION        NUM_NODES  STATUS
[REDACTED_CLUSTER_NAME]  us-west1-b  1.36.4-gke.1391002  1.36.4-gke.1391002  3          RUNNING
```

4. Verified the cluster and node-pool configuration:
```powershell
gcloud container clusters describe [REDACTED_CLUSTER_NAME] --project [REDACTED_PROJECT_ID] --zone us-west1-b --format="yaml(name,location,status,releaseChannel,initialClusterVersion,currentMasterVersion,currentNodeCount,nodePools.name,nodePools.version,nodePools.initialNodeCount,nodePools.autoscaling)"
```
```yaml
currentMasterVersion: 1.36.4-gke.1391002
currentNodeCount: 3
initialClusterVersion: 1.36.4-gke.1391002
location: us-west1-b
name: [REDACTED_CLUSTER_NAME]
releaseChannel:
  channel: REGULAR
status: RUNNING
```

```powershell
gcloud container node-pools describe default-pool --cluster [REDACTED_CLUSTER_NAME] --project [REDACTED_PROJECT_ID] --zone us-west1-b --format="yaml(name,version,initialNodeCount,autoscaling)"
```
```yaml
autoscaling:
  enabled: true
  maxNodeCount: 6
  minNodeCount: 2
initialNodeCount: 3
name: default-pool
version: 1.36.4-gke.1391002
```

5. Enabled managed Prometheus collection:
```powershell
gcloud container clusters update [REDACTED_CLUSTER_NAME] --project [REDACTED_PROJECT_ID] --zone us-west1-b --enable-managed-prometheus
```
```text
Updating [REDACTED_CLUSTER_NAME]...done.
Updated [https://[REDACTED_API_URL]].
```

6. Verified managed collection is enabled:
```powershell
gcloud container clusters describe [REDACTED_CLUSTER_NAME] --project [REDACTED_PROJECT_ID] --zone us-west1-b --format="yaml(name,monitoringConfig)"
```
```yaml
managedPrometheusConfig:
  enabled: true
name: [REDACTED_CLUSTER_NAME]
```

7. Checked kubectl authentication prerequisites:
```powershell
gcloud components list --filter="id:gke-gcloud-auth-plugin" --format="table(id,state.name)"; Get-Command kubectl -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source; Get-Command gke-gcloud-auth-plugin -ErrorAction SilentlyContinue | Select-Object -ExpandProperty Source
```
```text
Google Cloud CLI version: 589.0.0
ID                      Status
gke-gcloud-auth-plugin  Not Installed
C:\Program Files\Docker\Docker\resources\bin\kubectl.exe
Command exited with code 1 because the plugin was not installed.
```

8. Installed the missing GKE authentication plugin:
```powershell
gcloud components install gke-gcloud-auth-plugin
```
```text
No output.
```

9. Refreshed cluster credentials and created the requested namespace:
```powershell
gcloud container clusters get-credentials [REDACTED_CLUSTER_NAME] --project [REDACTED_PROJECT_ID] --zone us-west1-b
kubectl create namespace [REDACTED_NAMESPACE]
```
```text
Fetching cluster endpoint and auth data.
kubeconfig entry generated for [REDACTED_CLUSTER_NAME].
namespace/[REDACTED_NAMESPACE] created
```

10. Verified the namespace:
```powershell
kubectl get namespace [REDACTED_NAMESPACE] -o wide
```
```text
NAME       STATUS   AGE
[REDACTED_NAMESPACE]   Active   21s
```

11. Checked the lab folder before downloading:
```powershell
Get-ChildItem -Force labs\manage-kubernetes-in-google-cloud-challenge-lab | Select-Object Name,Length
```
```text
Name               Length
------------------  ------
command-history.md   2446
lab.md               1917
observations.md        86
```

12. Downloaded the sample manifest with the lab folder as the working directory:
```powershell
gcloud storage cp gs://[REDACTED_BUCKET_PATH]/prometheus-app.yaml .
```
```text
Copying gs://[REDACTED_BUCKET_PATH]/prometheus-app.yaml to file://./prometheus-app.yaml
Completed files 1/1 | 1.1kiB/1.1kiB
```

13. An additional PowerShell file metadata check was attempted but that terminal invocation did not recognize `Get-Item`; the workspace confirmed `prometheus-app.yaml` exists and its contents were readable.

14. Updated `prometheus-app.yaml` with the requested container settings:
```yaml
image: nilebox/prometheus-example-app:latest
name: prometheus-test
ports.name: metrics
```

15. Applied the Prometheus test Deployment to `[REDACTED_NAMESPACE]`:
```powershell
kubectl apply --namespace [REDACTED_NAMESPACE] --filename labs\manage-kubernetes-in-google-cloud-challenge-lab\prometheus-app.yaml
```
```text
deployment.apps/prometheus-test created
```

16. Downloaded the PodMonitoring sample with the lab folder as the working directory:
```powershell
gcloud storage cp gs://[REDACTED_BUCKET_PATH]/pod-monitoring.yaml .
```
```text
Copying gs://[REDACTED_BUCKET_PATH]/pod-monitoring.yaml to file://./pod-monitoring.yaml
Completed files 1/1 | 811.0B/811.0B
```

17. Updated `pod-monitoring.yaml` with the requested configuration:
```yaml
metadata.name: prometheus-test
labels.app.kubernetes.io/name: prometheus-test
matchLabels.app: prometheus-test
endpoints.interval: 45s
```

18. Applied the PodMonitoring resource to `[REDACTED_NAMESPACE]`:
```powershell
kubectl apply --namespace [REDACTED_NAMESPACE] --filename labs\manage-kubernetes-in-google-cloud-challenge-lab\pod-monitoring.yaml
```
```text
podmonitoring.monitoring.googleapis.com/prometheus-test created
```

19. Verified the Deployment, Pods, and PodMonitoring resource:
```powershell
kubectl get deployment,pods,podmonitoring --namespace [REDACTED_NAMESPACE] -o wide
```
```text
deployment.apps/prometheus-test   READY 3/3  AVAILABLE 3/3  IMAGE nilebox/prometheus-example-app:latest
pod/[REDACTED_POD_NAME]   1/1 Running   0 restarts
pod/[REDACTED_POD_NAME]   1/1 Running   0 restarts
pod/[REDACTED_POD_NAME]   1/1 Running   0 restarts
podmonitoring.monitoring.googleapis.com/prometheus-test   exists
```

20. Read back the live PodMonitoring configuration:
```powershell
kubectl get podmonitoring prometheus-test --namespace [REDACTED_NAMESPACE] -o yaml
```
```yaml
metadata:
  labels:
    app.kubernetes.io/name: prometheus-test
  name: prometheus-test
  namespace: [REDACTED_NAMESPACE]
spec:
  endpoints:
  - interval: 45s
    port: metrics
  selector:
    matchLabels:
      app: prometheus-test
status:
  conditions:
  - status: "True"
    type: ConfigurationCreateSuccess
```

21. Downloaded the demo deployment files with the lab folder as the working directory:
```powershell
gcloud storage cp -r gs://[REDACTED_BUCKET_PATH]/hello-app/ .
```
```text
Copied 11 files (18.3KiB) from gs://[REDACTED_BUCKET_PATH]/hello-app/.
The download included hello-app/manifests/helloweb-deployment.yaml.
Average throughput: 22.1KiB/s
```

22. Created the helloweb Deployment in `[REDACTED_NAMESPACE]` from the downloaded manifest:
```powershell
kubectl apply --namespace [REDACTED_NAMESPACE] --filename labs\manage-kubernetes-in-google-cloud-challenge-lab\hello-app\manifests\helloweb-deployment.yaml
```
```text
deployment.apps/helloweb created
```

23. Verified the Deployment and its Pod status using the CLI:
```powershell
kubectl get deployment helloweb --namespace [REDACTED_NAMESPACE]
kubectl get pods --namespace [REDACTED_NAMESPACE] -l app=hello,tier=web -o wide
```
```text
NAME       READY   UP-TO-DATE   AVAILABLE
helloweb   0/1     1            0

NAME                        READY   STATUS             RESTARTS
[REDACTED_POD_NAME]   0/1     InvalidImageName   0
```

24. Inspected the Pod error details from the CLI:
```powershell
kubectl describe pod --namespace [REDACTED_NAMESPACE] -l app=hello,tier=web
```
```text
Image:  <todo>
State:  Waiting
Reason: InvalidImageName
Warning InspectFailed: Failed to apply default image tag "<todo>": couldn't parse image name "<todo>": invalid reference format
Warning Failed: Error: InvalidImageName
```

25. Queried the Logs Explorer equivalent filter with exactly one resource type and one severity:
```powershell
gcloud logging read 'resource.type="k8s_pod" AND severity=WARNING' --project [REDACTED_PROJECT_ID] --freshness=1h --limit=10 --format="table(timestamp,resource.type,severity,jsonPayload.message,jsonPayload.reason)"
```
```text
resource.type: k8s_pod
severity: WARNING
jsonPayload.message: Error: InvalidImageName
jsonPayload.message: Failed to apply default image tag "<todo>": couldn't parse image name "<todo>": invalid reference format
```

26. Checked whether the requested log-based metric already existed:
```powershell
gcloud logging metrics describe pod-image-errors --project [REDACTED_PROJECT_ID] --format="yaml(name,filter,metricDescriptor.metricKind,metricDescriptor.valueType,description)"
```
```text
NOT_FOUND: Metric pod-image-errors does not exist.
```

27. Created the counter log-based metric using the validated Logs Explorer filter:
```powershell
gcloud logging metrics create pod-image-errors --project [REDACTED_PROJECT_ID] --description="Count Kubernetes Pod warning logs for the invalid image manifest" --log-filter='resource.type="k8s_pod" AND severity=WARNING'
```
```text
Created [pod-image-errors].
```

28. Verified the log metric:
```powershell
gcloud logging metrics describe pod-image-errors --project [REDACTED_PROJECT_ID] --format="yaml(name,filter,metricDescriptor.metricKind,metricDescriptor.valueType,description)"
```
```yaml
description: Count Kubernetes Pod warning logs for the invalid image manifest
filter: resource.type="k8s_pod" AND severity=WARNING
metricDescriptor:
  metricKind: DELTA
  valueType: INT64
name: pod-image-errors
```

29. Created the `Pod Error Alert` policy with a 10-minute Count/Sum threshold, trigger count 1, threshold greater than 0, and no notification channels:
```powershell
gcloud monitoring policies create --project [REDACTED_PROJECT_ID] --display-name="Pod Error Alert" --combiner=OR --condition-display-name="pod-image-errors above 0" --condition-filter='metric.type="logging.googleapis.com/user/pod-image-errors" AND resource.type="k8s_pod"' --aggregation='{"alignmentPeriod":"600s","perSeriesAligner":"ALIGN_COUNT","crossSeriesReducer":"REDUCE_SUM"}' --duration=0s --if="> 0" --trigger-count=1
```
```text
Created alert policy [projects/[REDACTED_PROJECT_ID]/alertPolicies/[REDACTED_POLICY_ID]].
```

30. Verified the alert policy:
```powershell
gcloud monitoring policies describe [REDACTED_POLICY_ID] --project [REDACTED_PROJECT_ID] --format=json
```
```text
displayName: Pod Error Alert
enabled: true
notificationChannels: empty (the response omitted the field)
conditionThreshold.filter: metric.type="logging.googleapis.com/user/pod-image-errors" AND resource.type="k8s_pod"
conditionThreshold.aggregations[0].alignmentPeriod: 600s
conditionThreshold.aggregations[0].perSeriesAligner: ALIGN_COUNT
conditionThreshold.aggregations[0].crossSeriesReducer: REDUCE_SUM
conditionThreshold.comparison: COMPARISON_GT
conditionThreshold.duration: 0s
conditionThreshold.trigger.count: 1
```
The create command set the threshold to `0` with `--if="> 0"`; the Monitoring API response omits the default-zero `thresholdValue` field.

31. Replaced the image placeholder in `hello-app/manifests/helloweb-deployment.yaml`:
```yaml
image: us-docker.pkg.dev/google-samples/containers/gke/hello-app:1.0
```

32. Validated the updated manifest with a server-side dry run:
```powershell
kubectl apply --dry-run=server --namespace [REDACTED_NAMESPACE] --filename labs\manage-kubernetes-in-google-cloud-challenge-lab\hello-app\manifests\helloweb-deployment.yaml
```
```text
deployment.apps/helloweb configured (server dry run)
```

33. Deleted the existing failing Deployment:
```powershell
kubectl delete deployment helloweb --namespace [REDACTED_NAMESPACE]
```
```text
deployment.apps "helloweb" deleted from [REDACTED_NAMESPACE] namespace
```

34. Created the updated Deployment:
```powershell
kubectl apply --namespace [REDACTED_NAMESPACE] --filename labs\manage-kubernetes-in-google-cloud-challenge-lab\hello-app\manifests\helloweb-deployment.yaml
```
```text
deployment.apps/helloweb created
```

35. Verified the rollout:
```powershell
kubectl rollout status deployment/helloweb --namespace [REDACTED_NAMESPACE] --timeout=180s
kubectl get deployment,pods --namespace [REDACTED_NAMESPACE] -l app=hello,tier=web -o wide
```
```text
deployment "helloweb" successfully rolled out
pod/[REDACTED_POD_NAME]   1/1   Running   0 restarts
```

36. Updated `hello-app/main.go` to report version `2.0.0`.

37. Compile-checked the Go application:
```powershell
Push-Location labs\manage-kubernetes-in-google-cloud-challenge-lab\hello-app
go test main.go
Pop-Location
```
```text
?       command-line-arguments  [no test files]
```
