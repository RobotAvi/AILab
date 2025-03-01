Thanks for https://vk.com/video-213615868_456239133

# n8n and Ollama Setup Script

This script helps you to install, start, stop, and uninstall n8n and Ollama Docker containers.

## Prerequisites

- Docker must be installed and running on your system.
- Python 3.x must be installed.

## Usage

1. **Install Services**

   To install n8n and Ollama, run the script with the `install` argument:

   ```sh
   python Start_n8n_and_ollama.py install
   ```

2. **Start Services**

   To start the n8n and Ollama services, run the script with the `start` argument:

   ```sh
   python Start_n8n_and_ollama.py start
   ```

3. **Stop Services**

   To stop the n8n and Ollama services, run the script with the `stop` argument:

   ```sh
   python Start_n8n_and_ollama.py stop
   ```

4. **Uninstall Services**

   To uninstall n8n and Ollama, run the script with the `uninstall` argument:

   ```sh
   python Start_n8n_and_ollama.py uninstall
   ```

## Notes

- Ensure Docker is running before executing the script.
- The script will create a Docker network named `n8n-network`.
- The n8n data will be stored in a Docker volume named `n8n_data`.

## License

This project is licensed under the MIT License.