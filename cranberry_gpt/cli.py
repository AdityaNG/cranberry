"""CLI interface for cranberry_gpt project.

Be creative! do whatever you want!

- Install click or typer and create a CLI app
- Use builtin argparse
- Start a web application
- Import things from your .base module
"""

import time

import docker
import paramiko
from vncdotool import api

from .settings import settings


def create_container_with_extra_step(base_image, extra_step, new_image_name):
    """
    Create a new Docker container with an extra step and register it as a new
    image. Useful for MCTS

    Args:
        base_image (str): The base image to use.
        extra_step (str): The extra step to add.
        new_image_name (str): The name for the new Docker image.
    """
    client = docker.from_env()

    # Create a new container from the base image
    container = client.containers.create(base_image)

    # Add the extra step
    container.exec_run(f"bash -c '{extra_step}'")

    # Commit the changes as a new image
    new_image = container.commit(new_image_name)
    print(f"New image created: {new_image.id}")

    # Clean up the container
    container.remove()

    return new_image


def build_image_if_not_exists(client, image_name):
    try:
        client.images.get(image_name)
        print(f"Image {image_name} already exists.")
    except docker.errors.ImageNotFound:
        print(f"Building image {image_name}...")
        # docker build -t ubuntu-vnc -f DockerfileUbuntuVNC .
        client.images.build(
            path=settings, dockerfile="DockerfileUbuntuVNC", tag=image_name
        )
        print(f"Image {image_name} built successfully.")


def run_container(client, image_name):
    container = client.containers.run(
        image_name,
        detach=True,
        ports={"22/tcp": 2222, "5900/tcp": 5900},
        name="ubuntu-vnc",
    )
    print(f"Container started: {container.id}")
    return container


def wait_for_ssh(
    hostname, port, username, password, timeout=30
) -> paramiko.SSHClient:
    start_time = time.time()
    while time.time() - start_time < timeout:
        try:
            client = paramiko.SSHClient()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            client.connect(
                hostname,
                port=port,
                username=username,
                password=password,
                timeout=timeout,
                auth_timeout=timeout,
                banner_timeout=timeout,
            )
            print("SSH connection established.")
            return client
        except paramiko.ssh_exception.NoValidConnectionsError:
            time.sleep(1)
    raise TimeoutError("Timed out waiting for SSH connection")


def ssh_command(ssh_client, command):
    stdin, stdout, stderr = ssh_client.exec_command(command)
    return stdout.read().decode("utf-8").strip()


def take_screenshot(client, output_file):
    client.captureScreen(output_file)
    print(f"Screenshot saved as {output_file}")


def stop_container_if_running(client, container_name):
    try:
        container = client.containers.get(container_name)
        if container.status == "running":
            print(f"Stopping container: {container_name}")
            container.stop()
        print(f"Removing container: {container_name}")
        container.remove()
    except docker.errors.NotFound:
        print(f"Container {container_name} not found.")


def main():
    client = docker.from_env()
    image_name = "ubuntu-vnc"

    # Build the image if it doesn't exist
    build_image_if_not_exists(client, image_name)

    # Stop and remove the container if it's already running
    stop_container_if_running(client, image_name)

    # Run the container
    container = run_container(client, image_name)

    time.sleep(5)

    try:
        # Wait for SSH to be available
        print("Awaiting SSH")
        ssh_client = wait_for_ssh(
            settings.SSH_HOST,
            settings.SSH_PORT,
            settings.SSH_USERNAME,
            settings.SSH_PASSWORD,
        )

        print("Awaiting GUI")
        vnc_client = api.connect(f"{settings.VNC_HOST}::{settings.VNC_PORT}")

        # Run CLI command
        print("Running CLI")
        output = ssh_command(
            ssh_client,
            "echo HelloWorld > ~/Desktop/output.txt && cat ~/Desktop/output.txt",  # noqa
        )
        print(f"CLI Output: {output}")

        # Wait a bit for the file to be created and the desktop to update
        time.sleep(5)

        # Take a screenshot
        take_screenshot(vnc_client, "desktop_screenshot.png")

    finally:
        # Clean up
        container.stop()
        container.remove()
        print("Container stopped and removed.")

        vnc_client.disconnect()
        ssh_client.close()


if __name__ == "__main__":
    main()
