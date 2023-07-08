
# Docker Commands

I assume Docker is already installed and "sudo" isn't necessary (ubuntu usually needs it).
Anyways, use `Docker command --help` for the complete list.


## Run a container

1. You have to pull the image, so: ` docker pull $imageName` 
    
    - Then, if the app you pulled needs, you have to create directories or configuration files.
2. You create a container running the image with: ` docker run $imageName` 
    > Will return an exadecimal string, that's the Container ID

3. On your IP and the app's port, you can access to the service 

### See the running container
With `docker ps`  we can see all the container running on our machine.
To stop one: 'docker stop $ContainerID' 

### List all images
List all the pulled image `docker image ls`


### Example

1. ` docker pull jellyfin/jellyfin:latest`  
> where :latest means the version we want
2. ` mkdir -p /srv/jellyfin/{config,cache}` 
> specific directories for jellyfin only
3. ` docker run -d -v /srv/jellyfin/config:/config -v /srv/jellyfin/cache:/cache -v /media:/media --net=host jellyfin/jellyfin:latest` 
4. localhost:8096/web/index.html and here we go.



### Flags/Option
You can configure/personalize a container passing it some parameters.. The parameters can be articolated with two "level" (see the -v flag)
#### Important flag

- d -> run the container in background (shell will be free to use) and print the container ID
- v -> use a volume container
    (second level) --volume list



## Start containers automatically
Restart policies allows a container to start automatically when it stops or when Docker restart.

Restart policies are different from `--live-restore` which keeps container alive during a Docker upgrade.


On the `docker run` command use the `--restart` flag following by:
- 'no', default not restart container
- 'on-failure', restart if the container exit due to an error
- 'always', the container starts again if exit due to an error or if Docker daemon restart
- 'unless-stopped', similar to always except if manually stopped or Docker daemon restarts.

eg. `docker run -d --restart unless-stopped` 

## Networking

- **bridge**: is default, your app is in a standalone container and needs to communicate
- **host**: remove the network isolation beetween the container and the docker host
- **overlay**: connect multiple Docker daemons togheter and enable swarm services to communicate with each other.
- **ipvlan**: gives user total control of IPv4 and IPv6 of the app, 
- **macvlan**: allows to give a mac address to a container

### Summary

- bridge -> is the best when your containers need to communicate on the same Docker host
- host -> is the best when the network stack souldn't be isolated from the docker host, but you want other aspect of the container to be isolated