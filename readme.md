```markdown
# n8n & Ollama Docker Management Script

This Python script simplifies the management of Docker containers for [Ollama](https://ollama.com) (an AI model runner) and [n8n](https://n8n.io) (a workflow automation tool). It allows you to install, start, stop, and uninstall these services with a simple menu-driven interface.

## Useful links
Thanks for https://vk.com/video-213615868_456239133 (hello world with n8n)
Ollama models https://ollama.com/library

## Features

- Installs and configures Ollama and n8n as Docker containers.
- Pulls the `llama3.2` model for Ollama automatically.
- Starts and stops services as needed.
- Creates a Docker network (`n8n-network`) for communication between containers.
- Opens the n8n web interface in your browser after starting.
- Provides a status check for containers and configuration.

## Prerequisites

- [Docker](https://www.docker.com/get-started) must be installed and running on your system.
- Python 3.x must be installed.
- Basic command-line knowledge.

## Installation

1. Clone or download this repository:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Ensure Docker is running:
   ```bash
   docker --version
   ```

3. Run the script:
   ```bash
   python script.py
   ```

## Usage

The script provides a menu with the following options:

1. **Install and Start n8n and Ollama in Docker**
   - Sets up the `n8n-network` Docker network.
   - Installs Ollama with the `llama3.2` model.
   - Installs n8n with persistent data and input volumes.
   - Starts both services and opens `http://localhost:5678` (n8n UI) in your browser.

2. **Stop Services**
   - Stops both Ollama and n8n containers if they are running.

3. **Uninstall Services**
   - Stops and removes both containers and the `n8n-network` network.

4. **Check Configuration**
   - Displays the status of containers, network, and volumes.

5. **Exit**
   - Closes the script.

### Example
```bash
python script.py
```
```
n8n ollama Management Menu:
1. Install and Start n8n and ollama in docker
2. Stop Services
3. Uninstall Services
4. Check Configuration
5. Exit

Enter your choice (1-5): 1
```

## Configuration

The script uses the following constants (defined at the top of `script.py`):

- **Ollama:**
  - Container name: `ollama`
  - Port: `11434:11434`
  - Model: `llama3.2` (default, pulled during installation)

- **n8n:**
  - Container name: `n8n`
  - Port: `5678:5678`
  - Data volume: `n8n_data:/home/node/.n8n`
  - Input path: Mapped from the current directory (`./input`) to `/home/node/input`

- **Network:**
  - Name: `n8n-network`

You can modify these constants in the script to suit your needs (e.g., change ports or model names).

## Notes

- **Ollama Model Download:** The `llama3.2` model download may take time depending on your internet speed (it’s a few GBs). Be patient during the first run.
- **Custom Models:** To use a different Ollama model, edit the `install_ollama()` function and replace `llama3.2` with your preferred model name from [Ollama’s library](https://ollama.com/library).
- **Volumes:** The n8n data volume (`n8n_data`) persists workflows between container restarts. The input folder is mapped from your local machine.

## Troubleshooting

- **Docker not found:** Ensure Docker is installed and added to your PATH.
- **Port conflicts:** If `11434` (Ollama) or `5678` (n8n) are in use, stop the conflicting processes or change the ports in the script.
- **Permission denied:** Run the script with `sudo` if Docker requires elevated privileges.

Check container logs for more details:
```bash
docker logs ollama
docker logs n8n
```

## Contributing

Feel free to submit issues or pull requests if you’d like to improve this script (e.g., add progress bars, support more models, etc.).

## License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.
```
