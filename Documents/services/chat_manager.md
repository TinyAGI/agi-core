
# TinyAGI/services/chat_manager.py

## Overview

The `chat_manager.py` file defines the `ChatManager` class, which sets up a Flask application to handle chat interactions through API endpoints. It provides a dedicated interface for managing conversational AI interactions.

## Functionality

- **API Endpoint**:
    - `/chat`: Handles chat requests by processing user messages and generating assistant responses.
- **Agent Initialization**: Initializes the `AgentSystem` and retrieves the default agent based on configuration.
- **Error Handling**: Logs and returns errors encountered during chat operations.

## Key Components

- **__init__**: Initializes the `ChatManager` with the required configurations.
- **create_app**: Configures the Flask application and sets up the `/chat` route.

## Usage

Instantiate the `ChatManager` and create the Flask app to handle chat interactions.

```python
from TinyAGI.services.chat_manager import ChatManager

chat_manager = ChatManager(config_file='config/agent_config.json')
app = chat_manager.create_app()

if __name__ == '__main__':
    app.run(debug=True)
```

### Chat API Usage Example

- **Chat Endpoint**:

    ```bash
    curl -X POST http://localhost:5000/chat          -H "Content-Type: application/json"          -d '{"messages": [{"role": "user", "content": "Hello!"}], "stream": false}'
    ```

    **Response**:

    ```json
    {
      "response": "Hello! How can I assist you today?"
    }
    ```
