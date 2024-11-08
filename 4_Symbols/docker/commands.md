# Docker Commands to Build and Run a Dockerfile

## Build the Docker Image
To build a Docker image from a Dockerfile, use the following command:
```sh
docker build -t <image_name>:<tag> .
docker build -t porttester:latest .

```
Replace `<image_name>` with your desired image name and `<tag>` with the version tag (e.g., `latest`).

## Run the Docker Container
To run a Docker container from the built image, use the following command:
```sh
docker run -d -p <host_port>:<container_port> --name <container_name> <image_name>:<tag>

>>>>>>>>>>> 90 should not matter >>>> right handside destionation port (isntance1) easier naming
docker run -d -p 90:9090 --name porttester_ins1 porttester:latest
```
Replace `<host_port>` with the port on your host machine, `<container_port>` with the port inside the container, `<container_name>` with your desired container name, and `<image_name>:<tag>` with the name and tag of your image.

@rifaterdemsahin ➜ /workspaces/containerports/4_Symbols/docker (main) $ docker ps
CONTAINER ID   IMAGE               COMMAND           CREATED         STATUS         PORTS                                                              NAMES
550d6d0c2d5f   porttester:latest   "python app.py"   7 seconds ago   Up 6 seconds   80/tcp, 443/tcp, 8080/tcp, 0.0.0.0:90->9090/tcp, :::90->9090/tcp   porttester_ins1
@rifaterdemsahin ➜ /workspaces/containerports/4_Symbols/docker (main) $ 

https://stunning-space-palm-tree-6w5jqx74q5fr4q5-90.app.github.dev/
>>>> empyty page opens up

## Example
Here is an example of building and running a Docker image:
```sh
# Build the image
docker build -t porttester:latest .

# Run the container
docker run -d -p 90:8080 --name porttester_ins6 porttester:latest
```
In this example, the Docker image is named `myapp` with the `latest` tag, and the container is named `myapp_container`. The container's port 80 is mapped to port 8080 on the host machine.


