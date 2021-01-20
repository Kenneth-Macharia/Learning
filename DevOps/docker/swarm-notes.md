# Why swarm?

- Swarm is a container orchestrator that runs one or more containers across one or
  more servers/nodes, efficiently.
- Docker containers promise deployment of app like on a PaaS, but on any machine/host
  anywhere and the apps will run the same.
- However, Paas solution have additional services/features that manage multiple
  (could be thousands) containers/services deployed over mutiple servers.
- So how do we replicate the PaaS features i.e managing and automating the containers'
  lifecycle e.g scaling, starting & re-starting, updating, creating, re-creating
  on failure, deleting, replacing and ensuring zero downtime
  (blue/green deployments) etc.
- How to create and monitor cross-node virtual networks? How to ensure only trusted
  servers run our containers? How to store sensitive container data and ensure it
  is only accssed by the container/ servers intended for?
- Swarm allow deploying container into production reliably.
- _Swarm mode_ introduced in 2016 is a clustering solution bringing together
  different OSs/nodes/clusters together into a single manageable unit, that you
  can then orcherstrate the lifecycle of containers in.

  _Swarm Classic <v1.12, which ran inside the Docker server and repeated docker
  run commands on many containers_
  _Swarm mode is also not enabled by default in Docker_

## Swarm under the hood

- A swarm, which can comprise VMs or physical machines running Linux or Windows,
  contains: (Illust. @ Section7/Time5.48)

    1. Manager nodes: have a local DB called _Raft db_, which stores information
       and configs that enable them to be the authority inside the swarm. A swarm
       can have more that 1 manager node (but only one leader node), but they all
       keep a copy of the Raft db and encrypt data moving within the swarm
       _using the control plane_ which is how instructions for actions are sent
       around the swarm) to ensure they administer the swarm securely.
    2. Worker nodes: that execute the tasks required in the swarm by following
       instructions received from the manager nodes.

    _Manager nodes can also be worker node and vice versa vis a process of node
     promotion and demotion_

- `$ docker run` can only provision 1 container on the machine the CLI is running
  on and does not have the ability to implemenent the PaaS features mentioned
  above and is replaced by:

    `docker service --help` in swarm

- This allows adding feature to the service such as replicas (which are tasks).
- A service can have multiple tasks and each task will lauch a container. Where
  previously we spun an nginx container using `$ docker run`, with swarm, we can
  spin up an nginx service using `$ docker service create` with 3 nginx replicas
  and use the manager nodes to decide which nodes in the swarm gets which replicas

  _By default they are spread out evenly. Illust. @ Section7/Time6.19_

- A swarm manager node has the following services (API, orcherstrator,
  Allocator, Scheduler and Dispatcher) and a worker node has a worker and executor
  service. _Illust. @ Section7/Time7.44_

## Using Swarm clusters

`docker info` to check if swarm is enabled
`docker swarm init` to enable swarm
`docker swarm --help` to view more command options

- Enabling swarm also creates a single node (manager) swarm with all the swarm features.
- Other things done in the background include creating the security certificate
  and root-signing it, issuing the certificate for the first manager node and
  creating tokens of other nodes that will join the swarm. Also the Raft databse
  is created and all security data created for the swarm are encrypted (>v1.13)
  and stored in it.

`$ docker node ls` to view swarm nodes
`$ docker node --help` to view command options

- `$ docker service` in swarm replaces `docker run` which is a single and local
  host/node solution. For in a cluster, we dont care about individual nodes but
  rather we 'throw' services at a swarm and it sort everything out for us.

`$ docker service --help` to view command options
`$ docker service create` to start a new service _see --help for more options_

- Replicas means service_currently_running / services_specified_to_run, and swarm's
  goal is to always ensure they are matched. The service naming convention
  (if not specified) follows _docker's random container naming_.

`$ docker service ps {service}` shows the tasks within a service (a task runs a container)

- This also shows the node/server/host on which the task is running on. Their name
  (if not specified) is in the form `service_name.task_number`

`$ docker container ls` show the containers being run by the swarm tasks.Their
name (if not specified) will be in the form `task_name.task_id + random_number`.

- A swarm service cannot be stopped, so the only option is to remove the service
  from the cluster using:

  `$ docker serice rm {serice}`

## Scaling up a service

`$ docker service update` _see `--help`_ to scale up a service. This is designed
to change a service live to ensure its always up e.g

`docker service update {service} --{options} {option_value_to_set}`

- This is similar to `$ docker update` for single containers.

Also `$ docker service scale --help`

- Should any task/container in the swarm fail, then another is immediatly spun up
  to replace it.

## Multi-Node Swarm Clusters

- To create a multi-node cluster using different OSs is not possible with the
  local docker install, as that will provide only 1 OS, the localhost OS.
- We can provision the 3 nodes/VMs on a cloud platform or run three nodes locally
  via virtualization software e.g virtualBox and docker-machine and ensure they
  are connected and can communicate with each other.
- The cloud deployment is best as it closest replicates production environments.
- There is also the option to use Play with docker but this will only persist
  your environment for 4hrs and is only for testing and exploration.

## Creating a Multi-node Swarm Cluster

- Create 3 Ubuntu-Linux nodes on a cloud platform e.g Digital Ocean/Azure/AWS/GCP.
_<https://docs.docker.com/network/overlay/> (See port required for the nodes to comm)_

- Set up SSH keys and .ssh config files for them to ease working with them.

    _See lecture resources on how to_

- Install docker using the script on `get.docker.com` on all the nodes.
- Ensure the nodes can communicate with each other by opening the required firewall
  port _Lecture resources on how to_
- Enable swarm on all the nodes, _ensure to specify an IP address for the swarm
  service to advertise on_.
- Use the node's public IP since it's accessible by other servers and the other
  nodes we created as well.(If required by the cloud platform)
- The node you fire up swarm on will be the leader node, use it to add other nodes,
  by using either the worker token or manager token on the other nodes. This will
  determine what type on nodes they become in the swarm. You can also administer
  the swarm from it.

_Worker nodes have a `blank status` and non of the docker commands will work on them
 as they dont have priviledges to administer the swarm. Other managers have a
 `reacheable status`._

## Overlay Multi-host Networking

- This is the Swarm-wide bridge VPN for the containers to cross-host on and can
  access each other as if they were on the same sub-net.
- Creating the overlay VPN: `$ docker network create --driver overlay`
- This deals with intra-swarm communications only.
- There is the optional IPsec encryption on network creation but this is turned off
  by default for performance reasons.
- A service can be added to zero, one or more overlay networks depending on the
  application design e.g have a DB service on a back-end network, views on a
  front-end network and an API connecting the two on both networks.
- The services use their service names for DNS resolution.

_Services cannot be run in the foreground as they have to be handled by the
 orcherstrator (always in detach mode)_

_View their logs via: `$ docker service logs {service}`_ _See --help for options_

### Swarm Overlay Networking Demo

- Run the drupal app and its postgres DB as services on a multi-node swarm cluster
  using an overlay network:

    1. Have the cluster set (3-node on Azure)
    2. Create the overlay network:

        `$ docker network create --driver overlay {network_name}`

    3. Create the postgres service and add it to the above created network:

        `$ docker service create
            --name {name} --network {network_name}
            -e ENV_VAR=env_val {service_image}`

    4. Create the drupal service and add it to the same network:

        `$ docker service create --name {name}
            --network {network_name}
            -p host_port:container_port
            --replicas {#_of_replicas} {service_image}`

    5. Check the service processes: `$ docker service ps {service}` to see on
       which node the service is running on, then use that nodes external IP to
       access the application running on that node.

- Creating volumes & bind mounts in services uses a different format as that on
  containers:

    `--mount type=volume/bind_mount,source=vol-name` or `/bind_mount,target=path/to/file`

- Published ports in a swarm cluster need to be opened as well on the nodes for
  the swarm routing mesh to work.

## Routing Mesh (Load Balancing via the Virtual IP/ VIP)

- Allows an application running on one node in the cluster to be accessible from
  the other cluster nodes.
- It is an ingress/incoming network _default is swarm overlay network_, created
  automatically when either `$ docker swarm init` or `$ docker swarm join` is ran.
- It routes incoming packets to the proper task/container in a swarm service &
  spans all the cluster nodes.
- It listens & load balances incoming traffic on all the cluster nodes.
- The routing mesh funtionality:

    1. Container-to-container: In an overlay network, it uses a VIP as a
    communication interface between two app services, especially when one of the
    services has multiple replicas. This means the two services don't communicate
    directly using their IPs but rather, they go through the routing mesh VIP.
    This system is put in place by Swarm automatically to ensure the load is balanced
    across the service tasks.

    2. External swarm traffic can choose which node in the swarm to hit, as all
    nodes will be lsitening on the published ports for a particular service. The
    routing mesh, based on it's load balancer will send the traffic to the right
    task/container.

- The routing mesh ensures that we are not concerned with what node/server is
  running what service, because this might changed especially if the container/task
  fails and the swarm re-creates the service on a different node. Thus we need not
  be concerned about changing firewall or DNS setting when services keep changing
  nodes.

- Routing mesh load balancing is STATELESS (interaction instances are independent
  of each other e.g for sessions, auth, resposnses etc). It also a layer 3 load
  balancer, operating at the TCP and not DNS layer 4 and will not work for running
  the same webiste on the same node, swarm and port for example.
  You need an extra layer e.g NGINX or use Docker EE, which has a built in layer 4
  web proxy.

## Swarm Stacks (Production-Grade Compose)

- An abstraction layer added to swarm allowing the use of docker compose files
  _> v3_ to define services, networks and volumes.
- A stack is a combination of services declared in the compose file with their
  volumes and networks. This is different from services ran using `$ docker service`
- `$ docker stack` manages all the services automatically including allocating
  proper labels to each service and its corresponging resources e.g volumes.
- Stacks also handle creation of these objects automatically e.g overlay networks
  but we can create our own before hand and instruct the stack to use those instead.
- The command to use with stacks:

    `$ docker stack deploy <options> <stack_name>`

- Additional compose keys in stacks:

    1. `deploy` Includes swarm specific items e.g replicas, rolling updates,
        fail over etc, which are production concerns not considered in a dev env.

    _We however cannot use a build instruction in the compose file, which should
    never happen in a production swarm anyway; builds should happend at the CI stage_

- `$ docker compose` will ignore _deploy_ instructions in the compose file in a dev
  environment and `$ docker stack` will ingore the _build_ instruction in the
  compose file in production, thus enabling the use of one compose file.

- Stacks simplify the process of managing swarm services through a YAML file
  instead of having to type numerous service commands to spin them up.
- They can however manage one swarm only and the nodes within that swarm only.

    _Docker visulaizer which runs on port 8080 is a visualization of the state of
    the swarm (stack visulaization in lecture 71: (4:36) minutes)_

## Swarm Secrets _> Docker 1.113 raft DB is encrypted by default_

- Easy, secure and built in swarm solution for storing confidential data e.g app
  access keys, passwords etc that will be required by the service(s) that will run
  the app.
- They are first stored first in the swarm then assigned to services and only on
  the disks of manager nodes. They are then passed to the containers that needs
  _those assigned to the particular service_ them through the TLS secured control
  plane.
- Secrets look like files to containers but are actually in-memory ram files with
  the names we assigned to them.
- They are accessed at `/run/secrets/<secret_name>` or `/run/secrets/<secret_alias>`
  if using alises to reference the same secret.

## Working with Secrets in Services

1. In the swarm leader node terminal, set up the secrets:

    Create a secret: `$ echo "{secret}" | docker secret create {secret_name} -`

    We will type the password in terminal and echo it to the docker daemon to
    create it into a ram file with the name we specify, creating a secret.

    `$ docker secrets ls` : a docker inspect of a secret will still not reveal
    the key assigned to the secret. The only way is to access it under `/run/secrets`
    inside a running container that uses the secret.

    _Note typing the password as part of a terminal command will leave it exposed
    in the users terminal history.
    _You can clear the history when done or grep the contents for the particular
    command and delete it form the terminal history)_

2. Using postgres secrets for username and password to access the database used
  by an app.

    a) Create the two secrets as above e.g: psql_user and psql_password
    b) Create a postgres service and assign the secrets to it, such that all
       containers assigned to this service will use those secrets to access the
       database:

    `$ docker service create
        --name psql
        --secret psql_user
        --secret psql_password
        -e POSTGRES_USER_FILE=/run/secrets/psql_user
        -e POSTGRES_PASSWORD_FILE=/run/secrets/psql_password postgres`

    _Official docker images have the `_FILE` environment variable standard to enable
    passing the secrets to the containers as shown above_

3. You can add/ remove/ update the secrets assigned to a service using:

    `$ docker service update`

## Working with Secrets in Stacks

- You can define secret in compose files _> 3.1_ for use with stacks.
- The best way to define the secrets in the compose file is to _create them before
  hand_ in the _leader node CLI_ then define them by their names in `secrets`
  section of the compose file using the keyword `external`.
- You can use `file` as well but that is less secure.
- After defining them, then we assign the secrets to only the services that need
  them.
- Removing the stack, removes all the resources the stack created just like services:

    $ docker stack rm <stack_name>

## Service updates

- Docker updates service replicas on a rolling basis i.e shuts down one at a time,
  updates it then spins it up again with the new updates.
- Orcherstrators, even though doing the above as efficiently as possible, can only
  limit downtime but not prevent it, because complex services e.g database as often
  difficult to update without changing how they interact with other services around
  them.
- Simple app services however may update smoothly without further intervention.
- The best way to prevent downtime is through rigorous testing of the update process.
- A `$ docker stack deploy` is always considered an update, when the stack is
  already pre-existing, thus the the services are update to the new docker-compose
  file configs if changed.
- Swarm update examples:

    1.Image versions: `$ docker service update --image app: <new_version> <service_name>`
    2.Add an environment variable: `$ docker service update --env-add NODE_ENV=production`
    3.Remove a published port: `$ docker service --publish-rm 8080`
    5.Change number of replicas of two services: `$ docker service scale web=8 api=6`

    _Alot of these commands can be diasy chained e.g to changing a port
    `--publish-rm 8080 --publish-add 80:80`_

- For a stack: `$ docker stack deploy -c <new_yaml_file> <stack_name>` and updates
  will be done automatically.
- Should the containers in service become unbalanced across the available nodes,
  especially due to service updates.
- The below command will force swarm to re-balance the load by replacing the tasks,
  to follow the default initialization allocation schema:

    `$ docker service update --force <service_name>`

## Using Docker Registry with Swarm

- Works the same as localahost because all nodes can see `127.0.0.1:5000` thanks
  to the routing mesh.

- To run the registry:

    `$ docker service create --name registry --publish 5000:5000 registry`

_All nodes in the swarm must be able to access the image in the registry._
