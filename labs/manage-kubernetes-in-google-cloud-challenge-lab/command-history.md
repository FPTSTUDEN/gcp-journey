# Command history

Append commands and their relevant outputs here. Redact secrets before saving.

**Command history and output**

1. Checked the active project and account:
```powershell
gcloud config get-value project
gcloud auth list --filter=status:ACTIVE --format="value(account)"
```
```text
qwiklabs-gcp-02-f7a5ce40a8a1
student-00-ed45ded90053@qwiklabs.net
```

2. Checked whether the cluster already existed:
```powershell
gcloud container clusters describe hello-world-kmtf --zone us-west1-b --project qwiklabs-gcp-02-f7a5ce40a8a1 --format="yaml(name,location,status,releaseChannel,autoscaling,currentNodeCount,currentMasterVersion)"
```
```text
ERROR: ... code=404 ... No cluster named 'hello-world-kmtf' in qwiklabs-gcp-02-f7a5ce40a8a1.
```

3. Created the cluster:
```powershell
gcloud container clusters create hello-world-kmtf --project qwiklabs-gcp-02-f7a5ce40a8a1 --zone us-west1-b --release-channel regular --num-nodes 3 --enable-autoscaling --min-nodes 2 --max-nodes 6
```
```text
Creating cluster hello-world-kmtf in us-west1-b...done.
Created [https://container.googleapis.com/v1/projects/qwiklabs-gcp-02-f7a5ce40a8a1/zones/us-west1-b/clusters/hello-world-kmtf].

CRITICAL: ACTION REQUIRED: gke-gcloud-auth-plugin ... was not found or is not executable.
kubeconfig entry generated for hello-world-kmtf.

NAME              LOCATION    MASTER_VERSION      NODE_VERSION        NUM_NODES  STATUS
hello-world-kmtf  us-west1-b  1.36.4-gke.1391002  1.36.4-gke.1391002  3          RUNNING
```

4. Verified the cluster and node-pool configuration:
```powershell
gcloud container clusters describe hello-world-kmtf --project qwiklabs-gcp-02-f7a5ce40a8a1 --zone us-west1-b --format="yaml(name,location,status,releaseChannel,initialClusterVersion,currentMasterVersion,currentNodeCount,nodePools.name,nodePools.version,nodePools.initialNodeCount,nodePools.autoscaling)"
```
```yaml
currentMasterVersion: 1.36.4-gke.1391002
currentNodeCount: 3
initialClusterVersion: 1.36.4-gke.1391002
location: us-west1-b
name: hello-world-kmtf
releaseChannel:
  channel: REGULAR
status: RUNNING
```

```powershell
gcloud container node-pools describe default-pool --cluster hello-world-kmtf --project qwiklabs-gcp-02-f7a5ce40a8a1 --zone us-west1-b --format="yaml(name,version,initialNodeCount,autoscaling)"
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
gcloud container clusters update hello-world-kmtf --project qwiklabs-gcp-02-f7a5ce40a8a1 --zone us-west1-b --enable-managed-prometheus
```
```text
Updating hello-world-kmtf...done.
Updated [https://container.googleapis.com/v1/projects/qwiklabs-gcp-02-f7a5ce40a8a1/zones/us-west1-b/clusters/hello-world-kmtf].
```

6. Verified managed collection is enabled:
```powershell
gcloud container clusters describe hello-world-kmtf --project qwiklabs-gcp-02-f7a5ce40a8a1 --zone us-west1-b --format="yaml(name,monitoringConfig)"
```
```yaml
managedPrometheusConfig:
  enabled: true
name: hello-world-kmtf
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
gcloud container clusters get-credentials hello-world-kmtf --project qwiklabs-gcp-02-f7a5ce40a8a1 --zone us-west1-b
kubectl create namespace gmp-uf9w
```
```text
Fetching cluster endpoint and auth data.
kubeconfig entry generated for hello-world-kmtf.
namespace/gmp-uf9w created
```

10. Verified the namespace:
```powershell
kubectl get namespace gmp-uf9w -o wide
```
```text
NAME       STATUS   AGE
gmp-uf9w   Active   21s
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
gcloud storage cp gs://spls/gsp510/prometheus-app.yaml .
```
```text
Copying gs://spls/gsp510/prometheus-app.yaml to file://./prometheus-app.yaml
Completed files 1/1 | 1.1kiB/1.1kiB
```

13. An additional PowerShell file metadata check was attempted but that terminal invocation did not recognize `Get-Item`; the workspace confirmed `prometheus-app.yaml` exists and its contents were readable.

14. Updated `prometheus-app.yaml` with the requested container settings:
```yaml
image: nilebox/prometheus-example-app:latest
name: prometheus-test
ports.name: metrics
```

15. Applied the Prometheus test Deployment to `gmp-uf9w`:
```powershell
kubectl apply --namespace gmp-uf9w --filename labs\manage-kubernetes-in-google-cloud-challenge-lab\prometheus-app.yaml
```
```text
deployment.apps/prometheus-test created
```

16. Downloaded the PodMonitoring sample with the lab folder as the working directory:
```powershell
gcloud storage cp gs://spls/gsp510/pod-monitoring.yaml .
```
```text
Copying gs://spls/gsp510/pod-monitoring.yaml to file://./pod-monitoring.yaml
Completed files 1/1 | 811.0B/811.0B
```

17. Updated `pod-monitoring.yaml` with the requested configuration:
```yaml
metadata.name: prometheus-test
labels.app.kubernetes.io/name: prometheus-test
matchLabels.app: prometheus-test
endpoints.interval: 45s
```

18. Applied the PodMonitoring resource to `gmp-uf9w`:
```powershell
kubectl apply --namespace gmp-uf9w --filename labs\manage-kubernetes-in-google-cloud-challenge-lab\pod-monitoring.yaml
```
```text
podmonitoring.monitoring.googleapis.com/prometheus-test created
```

19. Verified the Deployment, Pods, and PodMonitoring resource:
```powershell
kubectl get deployment,pods,podmonitoring --namespace gmp-uf9w -o wide
```
```text
deployment.apps/prometheus-test   READY 3/3  AVAILABLE 3/3  IMAGE nilebox/prometheus-example-app:latest
pod/prometheus-test-56f94bf745-hqbpf   1/1 Running   0 restarts
pod/prometheus-test-56f94bf745-kq49r   1/1 Running   0 restarts
pod/prometheus-test-56f94bf745-zpf65   1/1 Running   0 restarts
podmonitoring.monitoring.googleapis.com/prometheus-test   exists
```

20. Read back the live PodMonitoring configuration:
```powershell
kubectl get podmonitoring prometheus-test --namespace gmp-uf9w -o yaml
```
```yaml
metadata:
  labels:
    app.kubernetes.io/name: prometheus-test
  name: prometheus-test
  namespace: gmp-uf9w
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
gcloud storage cp -r gs://spls/gsp510/hello-app/ .
```
```text
Copied 11 files (18.3KiB) from gs://spls/gsp510/hello-app/.
The download included hello-app/manifests/helloweb-deployment.yaml.
Average throughput: 22.1KiB/s
```

22. Created the helloweb Deployment in `gmp-uf9w` from the downloaded manifest:
```powershell
kubectl apply --namespace gmp-uf9w --filename labs\manage-kubernetes-in-google-cloud-challenge-lab\hello-app\manifests\helloweb-deployment.yaml
```
```text
deployment.apps/helloweb created
```

23. Verified the Deployment and its Pod status using the CLI:
```powershell
kubectl get deployment helloweb --namespace gmp-uf9w
kubectl get pods --namespace gmp-uf9w -l app=hello,tier=web -o wide
```
```text
NAME       READY   UP-TO-DATE   AVAILABLE
helloweb   0/1     1            0

NAME                        READY   STATUS             RESTARTS
helloweb-68cb88c878-b7bzq   0/1     InvalidImageName   0
```

24. Inspected the Pod error details from the CLI:
```powershell
kubectl describe pod --namespace gmp-uf9w -l app=hello,tier=web
```
```text
Image:  <todo>
State:  Waiting
Reason: InvalidImageName
Warning InspectFailed: Failed to apply default image tag "<todo>": couldn't parse image name "<todo>": invalid reference format
Warning Failed: Error: InvalidImageName
```