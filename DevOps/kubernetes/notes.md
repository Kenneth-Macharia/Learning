# Kubernetes (K8s)

- One of the two most popular container orchestrators (Swarm is the other)
- Released in 2015 by Google but now maintained by an open source community.
- It is a set of APIs, that runs on apps in containers, to manage a set of servers, and
    execute the containers on docker by default, but it can run other container runtimes
    like container D, not just the docker runtime. OS its a series of containers that
    manage the multi-node system it's controliing by providing the set of APIs and CLI tools.
- The CLI tool for K8s is kube control ($ kubectl), similar to $ docker on swarm.
- The most common way to use K8s is via a cloud vendor, who will provide it as a SaaS and expose the API endpoints to use its tools locally or via a GUI that they may also provide.
- Another way is via K8s distribution packages offered by IaaS providers, who layers on top of the base open-source version, extra functionality to suit different use cases.

## Why K8s

- Just like Swarm, orchestration shines in automatically managing a frequently changing multi-container-multi-server environment, where the environment state need to be actively monitored to ensure it is as planned.

## Choosing K8s Solution

- Decision is between a cloud based solution or a vendor distribution that can be installed onsite, though pick a certified vendor to ensure that their distribution works well with the base API and is also cross-platform.

<https://kubernetes.io/partners/#conformance>

- K8s requires alot of vendor specific add-on to use easily, which the various vendors bundle in their distributions such a scustom auth, networking etc.
- The Github upstream version is usually the vanilla version and would probably be more difficult to use in production but is recommended to strat with when learning K8s.

## Swarm vs K8s

- Swarm is easier to use (developer oriented not just Ops), manage and low on resource requirements. It has 20% of the K8s feature, but it solves 80% of orchestration use cases.
    It being part of Docker, means it will run anywhere Docker will run which include legacy architectures such 32bit systems and even embedded systems like ARM bases systems or IoT. It is recommended for starting out.
- K8s is more feature rich and has a larger support community e.g every cloud vendor offers it. It is almost the de facto accepted orchestration solution, whether or not you require all its features ('No one ever got fired for buying IBM hardware')

## K8s Architecture

- At its core K8s is a set a API endpoints that allow interaction with via interaction tools, which are many but the ofiicial one is kubectl (kube control)
- It is used to configure and manage apps via the K8s API.
- As a whole, it is a series of containers, CLIs and configs.
- Servers in a K8s cluster are also called nodes.
- Kubelets are the containers agents that will run on the nodes and talk back to the K8s masters (control plane). These are needed because K8s runs on top of Docker thus facilitate the communication between the two, which was not needed on Swarm because Swarm is part of Docker.
- Control plane is a set of containers that manage the cluster which can be compared to manager nodes in Swarm. These however do a specific task that each specializes in as opposed to Swarm where the manager nodes can do any task in the cluster.

    _K8s cluster diagram vs Swarm cluster diagram: Lecture 96 - 4:10 min_

    _K8s use the same raft protocols as Swarm to maintain consensus, thus odd number master nodes are required._

- Each master node needs containers for controlling:

    1. etcd: a distributed storage for key-value pairs
    2. API: communicating and issuing cluster instruction
    3. scheduler: how and where the containers are placed in the nodes, in objects called pods.
    4. Controller manager: monitors the cluster state and reconciles with the task instructions passed to it.
    5. CoreDNS and any other depending on the add-ons installed

- Each node (worker node) needs a kublet:

    1. kube-proxy: controls the networking and any other depending on the options added

## Installing K8s

- There are numerous way to install K8s, the option used could be decided upon based on RAM utilization, ease to strat and shut down cluster, ease of restting the cluster environment, especially if tring K8s locally. See all options in Lecture 96.
- The easiest way to install locally is via the Docker desktop, since it's a free, checkbox enable/disable and will install kubectl automatically.
- If running on Linux e.g a cloud VM, use MicroK8s, which installs K8s and sets up everything you need to run it including the right version of kubectl. Install it using snap and not apt/yum, but snap can be installed via the two package managers. To use the kubectl command alone, however create an alias for your terminal, mapping kubectl to the default microk8s.kubectl.

_From March 2020, version 1.18 changed the kubectl run commands in use for previous versions (1.14 - 1.17), which are still default in many cloud platforms and Docker desktop._

- However, MicroK8s defaults to 1.18 so using K8s on a custom Linux install e.g a VM, will work differently but you can force installing v1.17 still:

    `$ sudo snap install microk8s --classic --channel=1.17/stable`

- Before using it, you'll need to enable the CoreDNS pod so it'll resolve service DNS names later:

    `$ microk8s.enable dns`

- Check the status of what is running in MicroK8s with:

    `$ microk8s.status`

## Using K8s

- A pod is one or more containers running together on one node and is the basic unit of deployment in K8s, with the containers always running inside a pod.
- Controllers are objects used to deploy and manage the pods and include Deployment, ReplicaSets, StatefulSet, DaemonSets, Jobs, CronJobs etc.
- Services (not similar to Swarm) are network endpoints for connectng to a set pods, at a certain DNS and port.
- Namespace is a filter for changing the kubectl view i.e limiting or exposing the features visible in the CLI view e.g defaults vs advanced.
- K8s is very unopinionated thus no 'right way' of doing things. Moreover is ever evolving and so is te CLI.
- Below are the 3 ways to create pods:

    `$ kubectl run` : for creating one pod only similar to $ docker run (exclusively in in v1.18), otherwise in v1.18- creates other resources as well e.g controllers.
    `$ kubectl create` : for creating resources via CLI or YAML
    `$ kubectl apply` : for use exclusively with YAML

- Run an nginx pod: `$ kubectl run my-nginx --image nginx`
- Check running running pods: `$ kubectl get pods`
- Check all created resources alongside a pod: `$ kubectl get all`

- The $ kubectl get all exposes the K8s container abstraction described above when we created the nginx pod i.e:

    1. a Deployment controller was created and within it;
    2. a ReplicaSet controller was created and within it;
    3. the number of replica pods specified at run time were created and within those;
    4. an nginx container was created, running the nginx image required

    See illustration in Lecture 101 - 6.50 min

_`$ kubectl run nginx --image nginx` creates a single pod named nginx in v1.18+._
_To create a deployment as above in v1.18+ use `$ kubectl create deployment nginx --image nginx`_

- To delete a deployment along with its resources:

    `$ kubectl delete deployment <deployment_name>`

_The service/kubernetes is the K8s server._

## Scaling ReplicaSets

- Using the scale command to scale the number of replica pods:

    `$ kubectl scale deployment <deployment_to_scale> --replicas <replicas_desired>`

_kubectl is flexible in the command formats in various areas e.g instead of `'deployment'` above `'deploy'` or `'deployments'` will still work. It is however not apparent in which cases such command variations can work. Recommendation is to choose one format and use it throughout._

- You can also use / instead of the space between the command and the option:
    `deployment/<deployment_name>`

## Inspecting Kubernetes objects

- Fetching kubernetes deployment logs:

    `$ kubectl logs deployment/<deployment_name>` but this only fetches the logs for one pod.

- To combine logs for all pods, use a 'selector' to fetch for all pods sharing a common label e.g. the deployment name (shared by all the pods):

    `$ kubectl logs -l run=<pods_common_label>`

_Be careful with label assignment as you may fetch data for pods not interested in. Also this selector system can only pull logs for up-to 5 pods in a deployment, as it is resource heavy. A third party tool in production e.g Stern is better epsecially for tail logging._

_Linux logging options: -- follow will refresh logs with new entries and `--tail` 1 will only output the last log entry_

- To view pod details (similar to docker's inpsect command) use the describe command:

    `$ kubectl describe pod/<full_pod_name>`  (get pod name using `$ kubectl get pods`)

- You can also inspect many pods at once (CAUTION WHEN THYE MANY) using:

    `$ kubectl describe pods`

- Kurbernetes just like any orchestration tool will automatically replace a pod to ensure the desired replicas are alwys maintained. To watch this process we can use the --watch linux command to obeserve this in action:

        $kubectl get pods --watch
        $kubectl delete pod/<pod_name_to_delete>

_Unlike swarm which will warn before editing or deleting the wrong object in the abstration layers, kubernetes will not, so extra care needs to be taking when modifying objects. Modification should be made top-down e.g modifying a deployment instead of any of the objects below it e.g ReplicaSet or pod._

## K8s Networking

- After creating a pod, you will need to create a service(s) on top of it, so that it can accept connections from within or without the cluster because they don't automatically have DNS resolving or have IP addresses attached to them.
- A service is an endpoint for pods i.e an address where the pods can be reached.
- To create a service for existng pods use:

    `$ kubectl expose`

- CoreDNS, a part of each master node in the control plane, allows service names to be resolved and it properly routes traffic to a service through one of the following 4 service types, the first two working out of thwe box with K8s:

    1. ClusterIP (default): only available within the cluster, pods can reach services on app port numbers.
    2. NodePort: for inter-cluster and external communication using the node IPs. This will create a high port on each node assigned to this service. Other pods need to be updated about this service and it's high (no-app default port).
    3. LoadBalancer: mostly used in the cloud for piping external traffic to the cluster and also used to control an external system e.g instructing an AWS load balancer to send traffic to the NodePort. It will also automatically create the previous two automatically, first. This only work with a infrastructure provider that allows their load balancers to receive instruction from K8s.
    4. ExternalName: as opposed to the 1st three above, this service is used for outbound cluster traffic. This is achived by creating CNAME DNS records in the CoreDNS serivice so that the cluster can resolve DNS names internally.

_Note that a LoadBalancer creates a NodePort and a NodePort creates a ClusterIP automatically._

## Creating a ClusterIP

- Use $ kubectl get pods -w to watch the service creation process in a seperate window.
- Start a httpenv deployment (a web server that returns the env variables on the host machine):

    `$ kubectl create deployment httpenv --image=bretfisher/httpenv`

- Scale up the deployment:

    `$ kubectl scale deployment/httpenv --replicas=5`

- Create the ClusterIP serivce and attach it to the above deployment, exposing port 8888 for intra-cluster communication:

    `$ kubectl expose deployment/httpenv --port 8888`

- Show services created:

    `$ kubectl get services`

_Remember that on MacOS and Windows, Docker runs a mini Linux VM on top of the host OS, unlike Linux, this means the container OS is the Host OS only on Linux. Since the ClusterIP service is only accessible inside the cluster, which technically is on a different host (the VM) as the host machine, we therefore can't access it directly from the host machine using `curl` for example._

- Accessing the httpenv deployment on Linux:

    `$ curl <service_IP>:8888`

- Acessing the deployment on Windows or Mac: Attempting the above will result in the following curl error `curl: (6) Could not resolve host: httpenv`. One way to get around this problem is to run a single pod within the deployment cluster (in the container host where the cluster is accessible), from within which we can access the ClusterIP serivce.

- Use a custom image with a bash utility from where we can run 'curl':

            $ kubectl run --generator=run-pod/v1 tmp-shell --rm -it --image bretfisher/netshoot -- bash

            1. Learn about generators later
            2. 'run-pod/v1 : generator template to use
            3. 'temp-shell' : pods name

## Creating a NodePort

- Expose a NodePort so that we can access it via the host IP (on all OSs).

    `$ kubectl expose deploymnet/httpenv --port 8888 --name httpenv-np --type Nodeport`

    _we specify a serivce type because this is not a default service like the ClusterIP service, which we did not need to specify it's type when creating it_

- A `$ kubectl get serivces` show a new service created. Note the port mapping format here is {container_port:host_port}, the opposite of that in swarm. The host_port is derived from a pre-set port range (30000 - 32767) defined in the container cluster for created NodePorts. They are set this high to avoid any port overlap in the host system.

    _<=1024 are privileged ports for use by the system root. >1024 are low ports and higly likely that some other service is using one of them_

    _More NodePort configs can be achieved via YAML only e.g specifying an exact port number, rather than having a random one assigned to it_

- Using the NodePort created above, we can then access our container in the cluster directly via `curl` unlike before with only the ClusterIP, where we had to run an additional container on the container host and access the cluster via the containers bash. VPN kit on docker desktop allows this to happen.

## Creating a LoadBalancer

- Expose a LoadBalancer serivce thay controls a cloud loadbalancer and accepts traffic into the cluster on a low port and routes that to a high port on the auto created NodePort, which then routes the traffic to the internal ClusterIP serivice and then to the right pod listening on the specified --port.

    `$ kubectl expose deployment/httpenv --port 8888 --name httpenv-lb --type LoadBalancer`

_Linux K8s distributions do not have a loadbalancer built in so this command will remain in *pending* state but the NodePort created will still work_

## Kubernetes Service DNS

- Since we are able to, example, `curl` a service by its name, it implies that there is a built in DNS server in kubernetes out-of-the box; CoreDNS is the default, providing DNS-Based Service Discovery.
- This mean getting a service host name, that matches the created service name, so that you can use the name to access the service, rather than using the FQDN (fully qualified domain name), which the host name is part of.
- Kubernetes provides `namespaces` as way to section of parts of a cluster, to enable creation of resources that share the same names i.e you can't create similar resources with similar names within the same cluster, but you can create sumilar resources within similar names within different namespaces, in the same cluster, includding DNS services.
- Namespaces prevent service clashes, but enable more modularized deployments at scale.
- To view namespaces:

    `kubectl get namespaces`

- A service FQDN has the following structure:

    `{hostname}.{namespace}.{SVC}.{cluster}.{local}`

- By default the {default} namespace is assigned to a basice cluster. `SVC` implies we are referring to a service and `cluster.local` is the default cluster name assigned to your basic cluster, but is configurable.

## Kubernetes Management Techniques

- Since K8s is lass opinionated aon how to use it's vast options, compared to Swarm, then the it begs the question of how best to use it in your workflow.
- `Generators` are helper templates that work behind commnds such as `$ kubectl run`, `$ kubectl expose` and `$ kubctl create`.
- Their purpose is to abstract the complex configs required when creating basic clusters using the above commands, by setting them to _defaults_ values.
- This also happens in other orchesration tool like swarm.
- Basically, they fill in the configs specified with the command options and other configs required but not specified as options are filled in with default values.
- Generator are versioned i.e. in what options they require and fill out.
- You can't list out all the generator templates available, but you can 'try' out a generator but not actually apply it to a cluster using the options `--dry-run -o yaml` to the above commands. This will demo what the effects of running the command would be and also outputs a yaml file for the configurations used.

    _The $ kubectl run command has been ear-marked for revision to remove alot of the create generators from it and leave those to other commands e.g 'create' or 'expose. This is to minimize the 'run' complexity and confusion where the command created different resources based on how it was used (SEE LECTURE 111). Going foward the 'run' commands will be used to only create pods_

## Imperative vs Declarative K8s Implementation

- Imperative means a step by step implemetation of instructions and focuses on how a tool operates. We achieve this by sequentially typing the K8s commands on th CLI to affect a cluster based on it's current state.
- This approach is easier to understanding a tool but difficult to automate.
- Declarative means focusing on what the a tool should accomplish without state information. In K8s, this is done using YAML files, which contains key/values for the instructions we want K8s to execute like in docker stacks.
- This allows for easier automation of the orchestration workflow and lead to `GitOps` happiness.

## Recommended K8s Mangement Approaches

- _First approach_ : using imperative commands such as run, create, expose, scale edit in the CLI, which is best for learning and small personal projects but hardest to manage over time.
- _Second approach_ : using the above imperative commands with a YAML file e.g

    `$ kubectl create -f file.yml` or `kubectl replace -f file.yml`

- The above is good ofr small production environments but still hard to autmate. Use git based yaml file to store changes.
- _Last approach_ : using a declarative approach with ONLY YAML files ie.

    `$ kubectl apply -f file.yml` or `$kubectl apply dir\

- You also use the 'diff' command to view changes to yaml files.
- This approach is best for production and easiest to automate but is harder to understand and predict effects of changes to the yml files, since we are not using an explicit command to affect a cluster e.g 'create'.

_It is important that that you dont mix the three approaches._

- The recommended workflow to using K8s is:

    1. Learn the imperative commands which will still be handy for local testing and troubleshooting.
    2. Move as quickly as possible to a full decarative implementation.
    3. Store yaml files in git or a git repo and commit every change before applying them.

- The above approach transitions you into GitOps, where yaml file changes commits are automatically applied to clusters.
