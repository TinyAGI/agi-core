# TinyAGI

TinyAGI is a modular Artificial General Intelligence (AGI) framework that allows dynamic loading of agents, plugins, and tools. It supports various AI models and can be extended to include new functionalities through plugins and tools.

## **Features**

- **Agent System**: Manage multiple AI agents with different models.
- **Plugin Manager**: Extend functionalities using plugins.
- **Tool Manager**: Integrate external tools (e.g., Wikipedia API).
- **Modular Architecture**: Easily add or remove components.
- **Dynamic Loading**: Load components from local files or GitHub repositories.

## **Setup Instructions**

1. **Clone the Repository**

   ```bash
   git clone https://github.com/your-username/TinyAGI.git
   ```

2. **Install Dependencies**

   ```bash
   cd TinyAGI
   pip install -r requirements.txt
   ```

3. **Configure Environment**

   - Rename `.env.example` to `.env` and add your OpenAI API key and other configurations.

4. **Run the Server**

   ```bash
   python run.py
   ```

## **Usage**

- **Running the Agent System**

  ```bash
  python run.py
  ```

- **Using the CLI**

  ```bash
  python -m TinyAGI.services.cli_manager generate --prompt "Your prompt here"
  ```

- **Accessing the API**

  - Start the server:

    ```bash
    python -m TinyAGI.services.server_manager
    ```

  - Send a POST request to `http://localhost:5000/chat` with the message data.

## **Contributing**

Contributions are welcome! Please submit a pull request or open an issue to discuss improvements.

## **License**

This project is licensed under the MIT License.
