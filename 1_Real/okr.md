# Objective and Key Results (OKRs)

## Objective
Create a robust and scalable Docker container that exposes multiple ports and facilitates seamless communication between different systems.

## Key Results
1. **Develop a Dockerfile**:
    - Create a `Dockerfile` that sets up a Python environment and exposes ports 80, 443, 8080, and 9090.
    - Ensure the Dockerfile includes necessary instructions to copy application files, install dependencies, and run the application.

2. **Build and Run Docker Container**:
    - Successfully build the Docker image using the created Dockerfile.
    - Run the Docker container and expose the specified ports to the host machine.

3. **Verify Port Exposure**:
    - Use Docker commands to verify that the ports 80, 443, 8080, and 9090 are correctly exposed and mapped to the host machine.
    - Ensure the application is accessible through these ports.

4. **Monitor Port Usage**:
    - Implement a logging mechanism to monitor and log any attempts to use the exposed ports.
    - Create a script (`log_ports.sh`) that logs port usage to a specified log file.

5. **Document the Process**:
    - Document the steps to create, build, and run the Docker container.
    - Provide clear instructions on how to verify port exposure and monitor port usage.

## Learning Source and Target
- **Source**: Utilize the provided Dockerfile and Flask application as a reference to understand the setup and configuration of a Docker container exposing multiple ports.
- **Target**: Apply the knowledge gained to create a similar Docker container for a different application, ensuring it meets the specified objectives and key results.
