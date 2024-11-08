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

docker run -d -p 90:9090 --name porttester porttester:latest
```
Replace `<host_port>` with the port on your host machine, `<container_port>` with the port inside the container, `<container_name>` with your desired container name, and `<image_name>:<tag>` with the name and tag of your image.

## Example
Here is an example of building and running a Docker image:
```sh
# Build the image
docker build -t myapp:latest .

# Run the container
docker run -d -p 8080:80 --name myapp_container myapp:latest
```
In this example, the Docker image is named `myapp` with the `latest` tag, and the container is named `myapp_container`. The container's port 80 is mapped to port 8080 on the host machine.