import os
import subprocess
import time
import webbrowser
import sys

# Constants for paths and container names
OLLAMA_CONTAINER_NAME = 'ollama'
N8N_CONTAINER_NAME = 'n8n'
OLLAMA_PORT = '11434:11434'
N8N_PORT = '5678:5678'
N8N_DATA_VOLUME = 'n8n_data:/home/node/.n8n'
N8N_INPUT_PATH = '/home/node/input'
N8N_NETWORK_NAME = 'n8n-network'

def run_command(command, check=False):
    """Executes command and returns result and return code"""
    result = subprocess.run(command, shell=True, text=True, capture_output=True)
    if result.returncode != 0:
        print(f"Command failed: {command}")
        print(f"Error: {result.stderr}")
        if check:
            sys.exit(1)
    return result.stdout.strip(), result.returncode

def check_container_exists(name):
    """Checks if container with specified name exists"""
    output, _ = run_command(f'docker ps -a --format "{{{{.Names}}}}"')
    return name in output.split('\n')

def check_container_running(name):
    """Checks if container with specified name is running"""
    output, _ = run_command(f'docker ps --format "{{{{.Names}}}}"')
    return name in output.split('\n')

def install_ollama():
    if not check_container_exists(OLLAMA_CONTAINER_NAME):
        print("Installing Ollama...")
        run_command(f'docker run -d --name {OLLAMA_CONTAINER_NAME} -p {OLLAMA_PORT} ollama/ollama', check=True)
        print("Ollama installed successfully")
    else:
        print("Ollama is already installed")

def install_n8n():
    if not check_container_exists(N8N_CONTAINER_NAME):
        print("Installing n8n...")
        current_dir = os.getcwd().replace('\\', '/')
        run_command(f'docker run -d --name {N8N_CONTAINER_NAME} -p {N8N_PORT} '
                   f'-v {N8N_DATA_VOLUME} -v "{current_dir}{N8N_INPUT_PATH}" '
                   f'docker.n8n.io/n8nio/n8n', check=True)
        print("n8n installed successfully")
    else:
        print("n8n is already installed")

def run_services():
    print("Starting services...")
    if not check_container_running(OLLAMA_CONTAINER_NAME):
        run_command(f'docker start {OLLAMA_CONTAINER_NAME}', check=True)
    if not check_container_running(N8N_CONTAINER_NAME):
        run_command(f'docker start {N8N_CONTAINER_NAME}', check=True)
    print("Services started")

def stop_services():
    print("Stopping services...")
    if check_container_running(OLLAMA_CONTAINER_NAME):
        run_command(f'docker stop {OLLAMA_CONTAINER_NAME}', check=True)
    if check_container_running(N8N_CONTAINER_NAME):
        run_command(f'docker stop {N8N_CONTAINER_NAME}', check=True)
    print("Services stopped")

def uninstall_services():
    print("Uninstalling services...")
    stop_services()
    if check_container_exists(OLLAMA_CONTAINER_NAME):
        run_command(f'docker rm {OLLAMA_CONTAINER_NAME}', check=True)
    if check_container_exists(N8N_CONTAINER_NAME):
        run_command(f'docker rm {N8N_CONTAINER_NAME}', check=True)
    run_command(f'docker network rm {N8N_NETWORK_NAME}', check=True)
    print("Services uninstalled")

# Rest of the code remains the same...
