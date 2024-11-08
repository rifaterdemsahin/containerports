# Creating a Container that Exposes Different Ports

In this guide, we will learn how to create a Docker container that exposes multiple ports and logs when another process tries to use them.

## Prerequisites

- Docker installed on your machine
- Basic knowledge of Docker commands

## Step-by-Step Instructions

### 1. Create a Dockerfile

Create a `Dockerfile` with the following content:

```Dockerfile
# Use an official Python runtime as a parent image
FROM python:3.8-slim

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make ports 80, 443, 8080, and 9090 available to the world outside this container
EXPOSE 80
EXPOSE 443
EXPOSE 8080
EXPOSE 9090

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]
```

### 2. Build the Docker Image

Run the following command to build the Docker image:

```sh
docker build -t my-python-app .
```

### 3. Run the Docker Container

Run the Docker container with the following command to expose ports 80, 443, 8080, and 9090:

```sh
docker run -p 8080:80 -p 8443:443 -p 8081:8080 -p 9091:9090 my-python-app
```

### 4. Verify the Ports

You can verify that the ports are exposed by running:

```sh
docker ps
```

You should see the ports `8080->80/tcp`, `8443->443/tcp`, `8081->8080/tcp`, and `9091->9090/tcp` listed.

### 5. Log Port Usage

To log when another process tries to use the exposed ports, you can use a simple script. Create a `log_ports.sh` script with the following content:

```sh
#!/bin/bash

while true; do
    netstat -tuln | grep -E '(:80|:443|:8080|:9090)' | grep -v 'LISTEN' >> /var/log/port_usage.log
    sleep 5
done
```

Run this script in the background:

```sh
chmod +x log_ports.sh
./log_ports.sh &
```

This script will log any attempts to use the specified ports to `/var/log/port_usage.log`.

## Conclusion

You have successfully created a Docker container that exposes multiple ports and logs when another process tries to use them. You can now access your application through the exposed ports and monitor port usage.
