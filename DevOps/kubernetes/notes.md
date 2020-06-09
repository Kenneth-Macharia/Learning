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
    5. Core DNS and any other depending on the add-ons installed

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