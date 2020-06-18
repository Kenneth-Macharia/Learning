# Kubernetes (K8s) Background
- One of the two most popular container orchestrators (Swarm is the other)
- Released in 2015 by Google but now maintained by an open source community.
- It is a set of APIs, that runs on apps in containers, to manage a set of servers, and
    execute the containers on docker by default, but it can run other container runtimes
    like container D, not just the docker runtime. OS its a series of containers that
    manage the multi-node system it's controliing by providing the set of APIs and CLI tools.
- The CLI tool for K8s is kube control ($ kubectl), similar to $ docker on swarm.
- The most common way to use K8s is via a cloud vendor, who will provide it as a SaaS and expose the API endpoints to use its tools locally or via a GUI that they may also provide.
- Another way is via K8s distribution packages offered by IaaS providers, who layers on top of the base open-source version, extra functionality to suit different use cases.

# Why K8s
- Just like Swarm, orchestration shines in automatically managing a frequently changing multi-container-multi-server environment, where the environment state need to be actively monitored to ensure it is as planned.

# Choosing K8s Solution
- Decision is between a cloud based solution or a vendor distribution that can be installed onsite, though pick a certified vendor to ensure that their distribution works well with the base API and is also cross-platform.

https://kubernetes.io/partners/#conformance

- K8s requires alot of vendor specific add-on to use easily, which the various vendors bundle in their distributions such a scustom auth, networking etc.
- The Github upstream version is usually the vanilla version and would probably be more difficult to use in production but is recommended to strat with when learning K8s.

# Swarm vs K8s
- Swarm is easier to use (developer oriented not just Ops), manage and low on resource requirements. It has 20% of the K8s feature, but it solves 80% of orchestration use cases.
    It being part of Docker, means it will run anywhere Docker will run which include legacy architectures such 32bit systems and even embedded systems like ARM bases systems or IoT. It is recommended for starting out.
- K8s is more feature rich and has a larger support community e.g every cloud vendor offers it. It is almost the de facto accepted orchestration solution, whether or not you require all its features ('No one ever got fired for buying IBM hardware')

# K8s Architecture
- At its core K8s is a set a API endpoints that allow interaction with via interaction tools, which are many but the ofiicial one is kubectl (kube control)
- It is used to configure and manage apps via the K8s API.
- As a whole, it is a series of containers, CLIs and configs.
- Servers in a K8s cluster are also called nodes.
- Kubelets are the containers agents that will run on the nodes and talk back to the K8s masters (control plane). These are needed because K8s runs on top of Docker thus facilitate the communication between the two, which was not needed on Swarm because Swarm is part of Docker.
- Control plane is a set of containers that manage the cluster which can be compared to manager nodes in Swarm. These however do a specific task that each specializes in as opposed to Swarm where the manager nodes can do any task in the cluster.

K8s cluster diagram vs Swarm cluster diagram: Lecture 96 - 4:10 min

(NB) K8s use the same raft protocols as Swarm to maintain consensus, thus odd number master nodes are required.

- Each master node needs containers for controlling:

    1. etcd: a distributed storage for key-value pairs
    2. API: communicating and issuing cluster instruction
    3. scheduler: how and where the containers are placed in the nodes, in objects called pods.
    4. Controller manager: monitors the cluster state and reconciles with the task instructions passed to it.
    5. CoreDNS and any other depending on the add-ons installed

- Each node (worker node) needs a kublet:

    1. kube-proxy: controls the networking and any other depending on the options added

# Installing K8s
- There are numerous way to install K8s, the option used could be decided upon based on RAM utilization, ease to strat and shut down cluster, ease of restting the cluster environment, especially if tring K8s locally. See all options in Lecture 96.
- The easiest way to install locally is via the Docker desktop, since it's a free, checkbox enable/disable and will install kubectl automatically.
- If running on Linux e.g a cloud VM, use MicroK8s, which installs K8s and sets up everything you need to run it including the right version of kubectl. Install it using snap and not apt/yum, but snap can be installed via the two package managers. To use the kubectl command alone, however create an alias for your terminal, mapping kubectl to the default microk8s.kubectl.

(NB) From March 2020, version 1.18 changed the kubectl run commands in use for previous versions (1.14 - 1.17), which are still default in many cloud platforms and Docker desktop.

- However, MicroK8s defaults to 1.18 so using K8s on a custom Linux install e.g a VM, will work differently but you can force installing v1.17 still:

    $ sudo snap install microk8s --classic --channel=1.17/stable

- Before using it, you'll need to enable the CoreDNS pod so it'll resolve service DNS names later:

    $ microk8s.enable dns

- Check the status of what is running in MicroK8s with:

    $ microk8s.status

# Using K8s
- A pod is one or more containers running together on one node and is the basic unit of deployment in K8s, with the containers always running inside a pod.
- Controllers are objects used to deploy and manage the pods and include Deployment, ReplicaSets, StatefulSet, DaemonSets, Jobs, CronJobs etc.
- Services (not similar to Swarm) are network endpoints for connectng to a set pods, at a certain DNS and port.
- Namespace is a filter for changing the kubectl view i.e limiting or exposing the features visible in the CLI view e.g defaults vs advanced.
- K8s is very unopinionated thus no 'right way' of doing things. Moreover is ever evolving and so is te CLI.
- Below are the 3 ways to create pods:

    $ kubectl run: for creating one pod only similar to $ docker run (exclusively in in v1.18), otherwise in v1.18- creates other resources as well e.g controllers.
    $ kubectl create: for creating resources via CLI or YAML
    $ kubectl apply: for use exclusively with YAML

- Run an nginx pod: $ kubectl run my-nginx --image nginx
- Check running running pods: $ kubectl get pods
- Check all created resources alongside a pod: $ kubectl get all

- The $ kubectl get all exposes the K8s container abstraction described above when we created the nginx pod i.e:

    1. a Deployment controller was created and within it;
    2. a ReplicaSet controller was created and within it;
    3. the number of replica pods specified at run time were created and within those;
    4. an nginx container was created, running the nginx image required

    See illustration in Lecture 101 - 6.50 min

(NB) $ kubectl run nginx --image nginx creates a singel pod named nginx in v1.18+. To create a deployment as above in v1.18+ use $ kubectl create deployment nginx --image nginx

- To delete a deployment along with its resources:

    $ kubectl delete deployment <deployment_name>

(NB) The service/kubernetes is the K8s server.

## Scaling ReplicaSets
- Using the scale command to scale the number of replica pods:

    $ kubectl scale deployment <deployment_to_scale> --replicas <replicas_desired>

(NB) kubectl is flexible in the command formats in various areas e.g instead of 'deployment' above 'deploy' or 'deployments' will still work. It is however not apparent in which cases such command variations can work. Recommendation is to choose one format and use it throughout.

- You can also use / instead of the space between the command and the option e.g
    deployment/<deployment_name>

## Inspecting Kubernetes objects
- Fetching kubernetes deployment logs:

    $ kubectl logs deployment/<deployment_name> but this only fetches the logs for one pod.

- To combine logs for all pods, use a 'selector' to fetch for all pods sharing a common label e.g. the deployment name (shared by all the pods):

    $ kubectl logs -l run=<pods_common_label>

(NB) Be careful with label assignment as you may fetch data for pods not interested in. Also this selector system can only pull logs for up-to 5 pods in a deployment, as it is resource heavy. A third party tool in production e.g Stern is better epsecially for tail logging.

(NB) Linux logging options: -- follow will refresh logs with new entries and --tail 1 will only output the last log entry

- To view pod details (similar to docker's inpsect command) use the describe command:

    $ kubectl describe pod/<full_pod_name>  (get pod name using $ kubectl get pods)

- You can also inspect many pods at once (CAUTION WHEN THYE MANY) using:

    $ kubectl describe pods

- Kurbernetes just like any orchestration tool will automatically replace a pod to ensure the desired replicas are alwys maintained. To watch this process we can use the --watch linux command to obeserve this in action:

    $ kubectl get pods --watch
    $ kubectl delete pod/<pod_name_to_delete>

(NB) Unlike swarm which will warn before editing or deleting the wrong object in the abstration layers, kubernetes will not, so extra care needs to be taking when modifying objects. Modification should be made top-down e.g modifying a deployment instead of any of the objects below it e.g ReplicaSet or pod.

# K8s Networking
- After creating a pod, you will need to create a service(s) on top of it, so that it can accept connections from within or without the cluster because they don't automatically have DNS resolving or have IP addresses attached to them.
- A service is an endpoint for pods i.e an address where the pods can be reached.
- To create a service for existng pods:

    $ kubectl expose

- CoreDNS, a part of each master node in the control plane, allows service names to be resolved and it porperly routes traffic to a service through one of the following 4 service types:

    1. ClusterIP (default): only available within the cluster, pods can reach service on app port numbers.
    2. NodePort: for inter-cluster and external communication using the node IPs. This will create a high port on each node assigned to this service. Other pods need to be updated about this service and it's high (no-app default port).

(NB) The above two services will work out of the box with kubernetes.

    3. LoadBalancer: mostly used in the cloud for piping external traffic to the cluster and also used to control an external system e.g instructing an AWS load balancer to send traffic to the NodePort. It will also automatically create the previous two automatically first. This only work with a infra provider that allows their load balancers to receive instruction from K8s.
    4. ExternalName: as opposed to the 1st three above, this service is used for outbound cluster traffic. This is achived by creating CNAME DNS records in the CoreDNS serivice so that the cluster can resolve DNS names internally.

## Creating a ClusterIP
- Use $ kubectl get pods -w to watch the service creation process in a seperate window.
- Start a httpenv deployment (a web server that returns the env variables on the host machine):

    $ kubectl create deployment httpenv --image=bretfisher/httpenv

- Scale up the deployment:

    $ kubectl scale deployment/httpenv --replicas=5

- Create the ClusterIP serivce and attach it to the above deployment, exposing port 8888 for intra-cluster communication:

    $ kubectl expose deployment/httpenv --port 8888

- Show services created:

    $ kubectl get service

(NB) Remember that on MacOS and Windows, Docker actually runs a mini Linux VM on top of the host OS, unlike Linux, this means the container OS is the Host OS only on Linux. Since the ClusterIP service is only accessible inside the cluster, whcih technically is on a different host (VM) as the host machine, we therefore can't access it direclt from the host machine using a curl for example.

- Accessing the httpenv deployment on Linux:

    $ curl <service_IP>:8888

- Acessing the deployment on Windows or Mac: Attempting the above will result in the following curl error 'curl: (6) Could not resolve host: httpenv'. One way to get around this problem is to run a single pod within the deployment cluster (in the container host where the cluster is accessible), from within which we can access the ClusterIP serivce.

- Use a custom image with a bash utility from where we can run 'curl':

    $ kubectl run --generator=run-pod/v1 tmp-shell --rm -it --image bretfisher/netshoot -- bash

(NB)    1. Learn about generators later
        2. 'run-pod/v1 : generator template to use
        3. 'temp-shell' : pods name