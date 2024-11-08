
# TinyAGI/services/server_manager.py

## Overview

The `server_manager.py` file sets up and runs the Flask server for the TinyAGI framework, exposing API endpoints for various functionalities such as chat, text generation, embedding, and configuration management.

## Functionality

- **API Endpoints**:
    - `/chat`: Handles chat interactions by processing user messages and generating responses.
    - `/generate`: Handles text generation requests based on provided prompts.
    - `/embed`: Generates embeddings for input data.
    - `/reload`: Reloads the model and configuration dynamically.
    - `/config`: Retrieves the current configuration.
- **Agent Initialization**: Initializes the `AgentSystem` and retrieves the default agent based on configuration.
- **Error Handling**: Logs and returns errors encountered during API operations.

## Key Components

- **create_app**: Configures the Flask application, sets up routes, and initializes the agent system.
- **run_server**: Starts the Flask server.

## Usage

Run the server to start handling API requests.

```python
from TinyAGI.services.server_manager import run_server

if __name__ == '__main__':
    run_server()
```

### API Usage Examples

- **Chat Endpoint**:

    ```bash
    curl -X POST http://localhost:5000/chat          -H "Content-Type: application/json"          -d '{"messages": [{"role": "user", "content": "Hello!"}], "stream": false}'
    ```

- **Generate Text Endpoint**:

    ```bash
    curl -X POST http://localhost:5000/generate          -H "Content-Type: application/json"          -d '{"prompt": "Tell me a joke.", "stream": false}'
    ```

- **Embed Endpoint**:

    ```bash
    curl -X POST http://localhost:5000/embed          -H "Content-Type: application/json"          -d '{"input": "Sample text for embedding."}'
    ```

- **Reload Configuration Endpoint**:

    ```bash
    curl -X POST http://localhost:5000/reload          -H "Content-Type: application/json"          -d '{"config_file": "config/new_config.json"}'
    ```

- **Get Configuration Endpoint**:

    ```bash
    curl -X GET http://localhost:5000/config
    ```
