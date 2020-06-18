# Docker Background
- Docker was released in 2013 as open source project.
- Major technological changes:
    1. Mainframes -> PC's
    2. Baremetal computing -> virtualization
    3. Data Centers -> Cloud computing
    4. Host -> Container computing including serverless

- These evolutions, before containerization, were mainly geared towards sys admins required learning new technologies and a mind-set change.
- Containerization was the first to include developers in the Ops mix and advancing the DevOps mind-set.

# Why Docker?
- Speed of software development.
- 'Matrix from hell' where different solution have their own unique requirments to work. Containers enable these solutions to work the same way regardless of their running environments.
- IT talent efficiency, by decreasing 80% maintainance time vs 20% innovation time, as a resutl of the multitude of existing software.
- Reduced compute power e.g needed for virtualization, means reduced provisioning costs.

# Docker editions/ versions
- Docker today is more thatn just a container runtime and evolves very quickly thus is important to keep up-to-date.
- There is a free CE (community edition) and a paid EE (enterprise edition)
- Installs are direct (Linux), Mac/Win (which require docker to install a VM on these OS for Docker to run on), Cloud (with all cloud offered features)
- Edge versions are betas which are released monthly as opposed to Stable versions released quarterly.

(NB) You can install docker desktop which come with all the tools bundled in (including the docker server) or just the docker CLI (via homebrew, for communication with docker on a remote server)

# Working with Docker containers
- Check docker version: $ docker version
- View command options: $ docker info
- Old command structure: docker <command> <option>
- New command structure: docker <mgt-command> <sub-command> <option>

(NB) More commands in tutorial commands text files.

- Image: is the application to be run.
- Container: an instance of an image running as a process. You can have many based on one image.
- Docker hub is Docker's default image registry.

## Demo: Spin up Nginx locally in a container:
$ docker container run --publish 80:80 nginx  (port format for -p HOST:CONTAINER)

1. Downloads the latest Nginx image from Docker hub if not available in local image cache
2. Starts a new container from the image above
3. --publish exposes/opens port 80 (can be any) on local machine and
4. routes traffic from the local port to the process running in the container at port 80 (Nginx being a web server listens on port 80 by default)

(NB) The image version can also be specified rather than using the default (latest) e.g nginx:1.11

## Stop a container using 'ctr + c' or $ docker container stop <container id> (first few characters of the ID will suffice.)

(NB) The ID will displayed when the container is run in detach mode i.e in the background (not displaying the process log in the console)

$ docker container run --publish --detach nginx

- Run an Nginx container with a custom name in detached mode:

$ docker container run --publish 80:80 --detach --name <custom_name> nginx

- List running containers: $ docker container ls
- List all docker containers: $ docker container ls -a
- List all local images: $ docker image ls

(NB) Container names, when one is not specified at runtime, are randomly generated from a concatenation of an adjective and the name of a notable hacker or scientist.

- Delete a stopped container: $ docker container rm <container ids> (space separated)
- Delete a running container: $ docker container rm --force <id>

- Pass environment variables to containers using the --env flag

## Monitor a container
- Commands to inspect and monitor Containers:

    1. $ docker container top: see process list inside a container
    2. $ docker container inspect: view container configs including how it started
    3. $ docker container stats: view container perfomance stats live

## Getting into a container
- Using Docker CLI, no SSH needed:
    1. $ docker container run -it: starts an interactive shell inside a container

(NB) The 'run' command has option to specify what the spun container will execute on start up. For nginx, the default is to run the nginx daemon, if no optional argument is specified i.e docker run -p 80:80 -d --name my_cont nginx

- By using -it flags (combination of -i and -t {see docker run --help for its options}), we can start a container with a bash prompt to enable interactivity with it ie:
docker run -it --name interactive_cont nginx bash.

- Note the program we require to run on container start must exist in the container either by default or as part of prior custom installation e.g

    $ docker run -it --name small_linux alpine bash,

    would fail because the alpine linux distribtion does not have bash installed by default.

    It does have sh so we could run:

    $ docker run --it --name small_linux alpine sh,

    then install bash using its package manager 'apk' then when next we run the previous command, it would work.

(NB) Quitting the bash prompt (or the program the container ran on start-up) also kills the container as well.

(NB) While -it is the flag for the 'run' command, for 'start' it is -ai (see docker start --help)

    2. $ docker container exec -it: run additional commands inside existing containers

    - To view an iteractive bash shell of a container already running another program e.g mysql or ngnix, use docker exec (See docker container exce --help for its options)

    docker exec --it <container_name> <additional_program_to_run> e.g:

    $ docker exec --it mysql bash

(NB) ## List running processes while in a container using 'ps or ps aux'. Note some container images dont inlcude it by defaultL install it using 'apt-get install -y procps'

- Note when exiting from an 'exec instance, the container is still alive, because the root process is still running in the container. The exec command add an additional to the container which is the one killed when exiting exec mode.

## Docker Networks
- Docker defaults work OK out of the box, but alot of those can be re-configured 'batteries included but removable'
- When a starting a container, it connects to a VPN (the 'bridge' network by default).
- Each of these networks that containers connect to route out through a NAT firewall (which the docker daemon configuring the host IP address on its default interface so that the containers can break out to the internet or the rest of the network)
- All containers within a host can talk to each other without the -p flag (--publish which exposes their ports)
- Best practice it to create a VPN for related processes of an app, so that they can communicate with each other, without exposing their port to the rest of the network.
- Some of the re-configurable defaults:

    1. Make new VPNS
    2. Attach containers to more than one VPN or none
    3. Forego the default VPNs and use the host IP i.e --net=host
    4. Use different docker network drivers to gain new abilities.

SEE DEMO DOCKER NETWORKING DIAGRAM IN LECTURE VIDEO 27

(NB) Use $ docker container port <container_name> to view which ports are fowarding traffic from the host to the container
- Containers do not always use the same IP address as the host.

- Docker networks CLI Management
    - Show networks: $ docker network ls
    - Inspect a network: $ docker network inspect
    - Create a network: $ docker network create --driver
    - Attach a container to a network: $ docker network connect
    - Detach a network from a container: $ docker network disconnect

(NB)    1. View command options for each above using --help
        2. The connect and disconnect command dynamically add and remove NICs (network interface controller / network cards) from a container.
        3. All docker networks are on the 172.0.0.0/16 subnet.
        4. All custom docker VPNs use the default 'bridge' driver. This can be changed using the --driver flag.

$ docker network ls outputs:
- docker 0, bridge is the default docker VPN NAT'ed behind the host IP (public IP)
- host is the network that skips the docker default VPN and attaches directly to the host interface using the --net=host flag. This foregoes some default docker network functionality including container security.
- none a network interface not connected to any network.

- Run a container and attach it to a specific network rather than the default bridge network using the --network flag:

$ docker container run -d --name webhost --network my_dk_vpn nginx

- Attach / detach containers dynamically to and from networks using the above commands.

- Security advantages of docker networks:

    1. With all tiers of an app sitting on the same container, their inter-communication never leaves the host
    2. All externally exposed ports are closed by default and must be manually exposed via the -p / --publish argument.

- DNS (doman name servers - internets phonebook) is key to inter-communication communication due to the dynamic nature of IP addresses within containers.

(NB) Using IPs for container communication is an anti-pattern and should be avoided.

- The docker daemon (program that runs docker in the background) has an built in DNS which containers use.

- Custom docker VPNs get automatic DNS resolutions for all containers within these networks. All containers in these networks can find each other using their names, regardless of their IP addresses.

- The default bridge network does not have this auto DNS resolution, the work around being to use the --link list when creating a container (see $ docker container create --help) to link the container to another, so its easier to just create a custom VPN.

# Working with Docker Images
- An image is the app binaries(No kernel or kernel modules such as drivers), its dependancies and the metadata about the image and how to run it.
- Officially though it is, an ordered collection of root filesystem changes and the corresponding execution parameters for use within a container runtime.
- The kernel that runs the image (via containers) is provided by the host.
- An image could small (one static binary file) or large (bundled with a linux distro, a web-server alongside your app and its dependancies etc)

## Docker Hub
- Normaly go for official images or hihgly downloaded and/or rated images on Docker hub.
- For dev and testing purposes it is OK to use the latest image version but for production stick to a specific version and use a DevOps tool to manage upgrades.
- Docker images are made up of union file system changes, layered on top of each other, with latest latest change being the top and final image change.

    $ docker history <image_name>: <version> outputs the layers making up an image, from inception to its current composition.

- Each layer is uniquely identified by a SHA hash as its image ID, ensuring only one copy of an image is pulled and stored locally, saving space, even if $ docker images or $ docker image ls show an images appearing more than once (they will all have the same ID).

    $ docker inspect <image_name>:<version> show the image metadata and the execution parameters.

- A container is also an image layer added when created/run but unlike the actual image composition layers which are read-only, the container layer is read-write.
- Only official images have root namespace, the unofficial image naming convention is:
    publishers_repo_name/unoffical_image_name
- To push images to your docker hub, you must be logged in via the dockr CLI:

    $ docker login

- This create a json in your local profile with the login details.Ensure to log out if the machine with these details is not trusted.

## Image tagging
- An image tag is a label pointing to a specific image ID. You can have many tags for the same image, but they all refer to one images, denoted by thier similar ID.
- You can tag any images either yours or other images, the tag however needs to be in a specific format to work with image repos.

    - $ docker image tag --help

- By retagging an image you can push it to your docker hub as a new image repo availble to the public (Remember to follow naming convention for none official image repos):

    $ docker image push <image_name:image_tag>

- This is convinient for customizing images quickly and since the layers inherited already exist, there will be no duplication, only csutomizations will be added.

(NB) If you dont specify your tag name, it defaults to latest. (On official image repos, 'latest' means the latest stable image which may not be the case on unofficial images)

- To make an image repo private, create the repo first, set is as private then push the image.

# Dockerfiles
- A Dockerfile is a text document that contains all the commands a user could call on the command line to assemble an image.
- They are shell script-like files composed of stanzas which are commands (and layers) that build on the image being created.
- Build an image using the files in the cwd (the context) (only include the files neccessary in here): https://docs.docker.com/engine/reference/builder/

    $ docker build .

- Start an image build using a file other than the default Dockerfile by using:

    $ docker build -f <path_to_dockerfile>

    The above uses a --file docker_file alias

- Specify the image repo and tag to store the image when the build completed:

    $ docker build -t <repo_name/image_name:tag> .

(NB) See also course repo files for DockerFile samples.

- All images must have a 'FROM' stanza usually inheriting a mininmal distribution but you can start from scratch using 'FROM scratch'
- Commands to be included as a single layer or to be run together are concatenated using '&&'.
- Container logging is handled by docker, so specify where to collect log files from your app for docker to collect and spit to stdout or stderr.
- By default docker does not expose any port and if your app need to expose ports, they must be specified under the EXPOSE stanza, but the -p flag must be specified when running a container off the image for the specified ports to actually be published.
- CMD is a required stanza and specifies what will be run when a container is spun up.
- The order of commands in the Dockerfile matters because, once the initial build of the image is done, docker keeps a record of the build process the cache, such that a rebuild of the image, only executes the stanzas where changes have been made and stanzas after that. To ensure builds are fast place commands for mostly static items at the top and those that change alot at the bottom of your Dockefile.

# Cleaning the Docker system (docker >=1.13)
- $ docker system --help to see system management flags
- $ docker system prune removes everything that is not associated to running containers.
- docker system df show resources list and info
- $ docker image prune will remove dangling images only
- $ docker container prune will remove unused containers
- $ docker system prune -a will removes all containers images and networks.
- $ docker volume rm <volume_name> removes one volume ($ docker volume prune removes all)

# Container Lifetime & persistent Data
- Containers are usually immutable (once created cannot be changed) and ephemeral (short-lasting and disposable). They can be created any number of times from an image.
- To handle the app data that changed over the lifetime of a container, Docker provides feature to separate the two i.e container immutability and app data mutability (separation of concerns)
- Even if a container is recycled/ updated, the container data is still persisted and is available to the 'new' container as it were for the 'old' one, a concept called persistent data and this features work automatically by default. Only when the container is removed, is its UFS file changes / persisted data removed as well.
- Docker features to handle persistant data are:

    1. Volumes: container config options that create special location outside the container UFS, to store its persistant data, and allow attaching the data to any container over container removals. To container they appear as its own local file path and not the hosts.

        - Volume configs are specified under the VOLUME stanza in the DockerFile.
        - $ docker volume ls : list the volumes created for a container and these out-live
            the container, thus if the container is deleted, the volumes remain.
        - If you inspect a container, then under Mounts, you see the mapping between the volume location in the container (specified in the DockerFile) and its actual location in the host (for mac & windows this can't be navigated to since they live in the VM autocreated for these two OSs).
        - The problem with the auto created volumes is that you can't tell which volume relates to which container.
        - Named Volumes help solve this problem. This is specified using the -v flag when running a container:

        $ docker container run -v <custom_vol_name>:<the_volume_config_in_the_DockerFile>

        - The above will create a named volume for the container and with a $ docker volume ls or $ docker volume inspect <vol_name> its easier to distinguish which volume realtes to which container and can also be confirmed by inspecting the container.

        - Removing the above container and creating another and assigning the above vol, a new vol will not be created but the previous one will be attached to the new container.

        (NB) Sometimes especially in production you may need to create a volume ahead of time to specify other custom config eg driver. This is done using:

        $ docker colume create: See the command options using --help

    2. Bind Mounts: linking a host file directory to a container's, also makes it look like a local file path to the container, essentially having two pointer to the same location on the host file system. These allow live editing of container files from outside the container becuase the two are linked.

        - The data persists while the bind mount exists and survives the container it was created for.
        - Bind mounts cant be specified in DockerFiles because they must exist on the host's hard drive thus are specified during run time eg:

        $ docker container run -v full_path/on/the/host:/path/in/container (unix)
        $ docker container run -v //c/full_path/on/the/host:/path/in/container (Win)

        - Docker knows this is a bind mount, rather than a named vol because it begins with a '/'

        Lecture 49 & 52/53: Live demos of how cool bind mounts are!

# Docker Compose
- Because we will frequently need to run multiple containers to solve a particular solution.
- Docker compose helps configure relationships between containers so that they cna work together easily to solve our problem.
- Enables one-liner developer env start-ups.
- Comprises of two parts:

    1. YAML config file (docker-compose.yml): similar but easier than a .ini file, that describes solution options for docker containers, networks, volumes, env variables etc. i.e automate the docker run options.

        - Default name docker-compose.yml but any other .yml file can be used alongside 'docker-compose -f'
        - Has its own versions, defaulting to v1 if not specified, recommmended >= v2 but to get the latest features specify the latest version.
        - Used with 'docker-compose' in dev/tesing and with 'docker' in production via Swarm(> v1.13)
        - See compose-sample-1 directory

    2. The compose CLI (docker-compose) particularly used for dev/testing YAML file automation. It is separatefrom the docker CLI and needs to be installed separate on Linux systems but is bundled together with the docker CLI for other platforms.

    https://docs.docker.com/compose/install/

        Access help via docker-compose --help

        - docker-compose up : sets up and starts a dev environment specified in the docker-compose.yml file i.e containers, volumes, networks etc.

        - docker-compose down : stops and tears down a dev environment that is running.

        - Use ctrl+c to temp stop the environment (so that the instances are not torn down) then simply use docker-compose up to start it up again.

        - Basically has similar comands to the docker run command (--detach etc) and can be used in a similar way to docker run only within the context of the YAML configs. It achieves this by communicating with the docker API on our behalf.

## Building images using Docker Compose at runtime
- Compose will build images with:

    $ docker-compose up if image is not found in the cache (See docker-compose2.yml)

- The above is a common developer set-up to build and test in a production simulated environment. Note a DB service or any other required service the applicationwill need in production can also be added.

- To rebuild already built images by docker-compose i.e if changes are made to it and since once build it remains in the cache unitl manually removed, use:

    $ docker-compose build or $ docker-compose up --build

(NB) docker-compose down does not clean up the image built above, to do this ensure an 'image' is not specified in the docker-compose file when building, then run:

    $ docker-compose down --rmi <option> (see docker-compose --help)

## Using Secrets with docker-compose
- Usin docker-compose > v11, it is possible to use secrets with the cli for development, only that you can only use secrets from a file stored locally on the host hard drive.
- This is not secure compared to secrets stored in a swarm, but allow us to mimick this production functionality to locally test our deployments.
- Other than the limitation to use secret files, the rest of the functionality is similar to secrets in swarm.

(NB) The docker-compse file version still needs to be >=v3.1

# Docker health Checks
- Introduced in Docker 1.12, this feature is available on the docker run and service commands as well as in Docker and docker-compose YAML files.
- The docker engine 'execs' the command in the container and returns either 0 (OK) or 1 (ERROR).
- Container states in terms of health are: starting, healthy or unhealthy.
- Prior to health checks, all docker knew about the container was that it is running, health introduces more checks like ensuring the docker is actually doing what it is supposed to do. (It is however not as robust as an external/3rd party monitoring tool)
- Health check appears:

    1. Under $ docker container ls
    2. Under $ docker container inspect

(NB) With $ docker run, it does not take any action against unhealthy container, but swarm will replace them when detected and if updating will wait for the health check to pass before proceeding to the next task.

- Examples of using health checks:

    1. Dockerfile:

    --interval=<duration(def: 30sec)>   :after how long the health checks(s) will be run
    --timeout=<duration(def: 30sec)>    :how long it waits before returning an error code
    --start-period=<duration(def: 0sec)>   :overrides the default interval period especially for apps that take longer to start.
    --retries=<N(default:3)>

    - Basic command example:

        HEALTHCHECK curl -f https://localhost/ || false

        HEALTHCHECK --timeout=2s --interval=3s --retries=3 CMD curl -f https://localhost/ || exit 1 (if giving options and the command comes after the options)

        HEALTHCHECK --interval=5s --timeout=3s CMD pg_isready -U postgres || exit 1

    (NB) Diffrent apps have differnt health check tools

    2. $ docker run \
        --health-cmd="curl -f localhost:9200/_cluster/health" false" \
        --health-timeout=5s \
        --health-start-period=2s \
        elasticsearch:2

        (NB) Shell commands usually output 1 incase the command returns an error, curl can return more than that so we specificy what it should return. This can be 1 or false.

    3. Compose files: (>=2.1 for health checks and >=3.4 for start_period)

        healthcheck:
            test: ["CMD", "curl", "-f', "http://localhost"]
            interval: 1m30s
            timeout: 10s
            retries: 3
            start_period: 3m

# Docker Registries
- Docker hub is the most popular docker container registry though not the only one.
- Docker hub includes other features such as image auto-builds.
- Via docker hub hooks you can extend your deployment workflow down the line e.g to the production server after successful image build.
- Via docker hub create and autobuild you can link to a code repo such as github and have docker hub build images on code pushes.
- For automated image builds, under build setting two setting of particular impotance:

    1. Repository links: add dependancy repos so that when those image dependancies get updated, your image get re-built as well.
    2. Build triggers: incase docker hub should listen for build triggers from other software.

## Docker Registry
- It is a private registry that can be used to store images on a private network and best suited for small teams.
- It is part of dockre/distribution github repo (not legacy) and is written in Go.
- It ca be accessed from docker hub: $ docker pull registry
- It is the de facto back end registry for storing images privately.
- It has basic auth, no GUI, it is at its core a web API running on port 5000 and a storage system locally, but has drivers for various cloud platform storage solutions.
- Key concerns working with dockr registry:

    1. Set up configs inclusing TLS for better security
    2. Garbage collection for disk space management
    3. Enabling docker hub cache via --registry-mirror so as not to pull all images from docker hub everytime they are required.

## Using Docker Registry Locally
- Docker need a registry to be secured using HTTPS before interacting with it, except if running on localhost (127.0.0.0/8)
- For remote self-signed TLS or no TLS, enable 'insecure-registry' in the engine to allow docker interaction but docker will still complain about the registry insecurity.
(https://training.play-with-docker.com/linux-registry-part1/)

- To run the registry: $ docker container run -d -- name registry -p 5000:5000 registry

- Tagging images for registries other Docker Hub, follow the format:

    $ docker tag image_name host/tag_name

- Push images to the registry: $ docker push <image_host/image_tag> (as used in above command)

- Pull images from the registry: $ docker pull <image_host/image_tag> (as used in above command)

- To stop the registry container: $ docker container kill registry
- To remove the registry: $ docker container rm registry

- To use a volume to store the registry data:

    $ docker container run -d --name registry -p 5000:5000 -v $(pwd)/registry_data:/var/lib/registry registry

## Using Docker Registry with Swarm
- Works the same as loclahost because all nodes can see 127.0.0.1:500 because of the routing mesh.

- To run the registry:

    $ docker service create --name registry --publish 5000:5000 registry

(NB) Note all the nodes in the swarm need to be able to access the image in the particular registry.

(NB) Use hosted SaaS registries over a private repo.

## Using Docker Registry over HTTPS: https://training.play-with-docker.com/linux-registry-part2/