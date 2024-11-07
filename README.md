## 🪧 NOTICE: "WORK IN PROGRESS" V.0.0.1

<p align="center">
  <img src="https://raw.githubusercontent.com/SullyGreene/TinyAGI/refs/heads/main/Static/logo.png" alt="TinyAGI Logo">
</p>


# 🧠 TinyAGI

**TinyAGI** is a powerful, modular Artificial General Intelligence (AGI) framework crafted for seamless integration and management of AI agents, plugins, and tools. With its adaptable and extensible architecture, TinyAGI enables dynamic loading of components from local and GitHub-hosted sources, empowering you to customize and scale for a multitude of use cases.

[![PyPI Version](https://img.shields.io/pypi/v/TinyAGI)](https://pypi.org/project/TinyAGI/) [![License](https://img.shields.io/badge/license-MIT-blue.svg)](https://github.com/SullyGreene/TinyAGI/blob/main/LICENSE) [![GitHub Stars](https://img.shields.io/github/stars/SullyGreene/TinyAGI?style=social)](https://github.com/SullyGreene/TinyAGI/stargazers) [![Twitter Follow](https://img.shields.io/twitter/follow/SullyGreene?style=social)](https://twitter.com/SullyGreene)

---

## 📖 **Table of Contents**

- [🧩 Features](#-features)
- [📦 Installation](#-installation)
- [🔧 Setup Instructions](#-setup-instructions)
- [🛠 Usage](#-usage)
- [📚 Documentation](#-documentation)
- [🧪 Testing](#-testing)
- [📝 Contributing](#-contributing)
- [🛡 License](#-license)
- [📞 Contact](#-contact)
- [🗺️ Roadmap](#-roadmap)

---

## 🧩 Features
  
  - 🌐 **Agent System**: Manage various AI agents, from OpenAI to Ollama and LLaMA.
  - 🔌 **Plugin Manager**: Seamlessly expand functionality with versatile plugins.
  - 🛠 **Tool Integration**: Use tools like the Wikipedia API to enhance capabilities.
  - 🔄 **Dynamic Loading**: Load components locally or clone from GitHub repositories on the fly.
  - 🚀 **Task Automation**: Orchestrate agents, plugins, and tools to define and execute complex tasks.
  - 📑 **Comprehensive Documentation**: Easily accessible Markdown files for every component.
  - 🔥 **Robust Error Handling**: Advanced logging and error management for smooth operation.

---

## 📦 Installation

### **From PyPI**

Get the latest TinyAGI in seconds with `pip`:

<details>
  <summary>Show command</summary>

  ```bash
  pip install TinyAGI
  ```
</details>

### **From GitHub**

Clone and set up dependencies:

<details>
  <summary>Show commands</summary>

  ```bash
  git clone https://github.com/SullyGreene/TinyAGI.git
  cd TinyAGI
  python setup_env.py
  ```

> **Note:** `setup_env.py` creates a `venv` environment, installs dependencies, and downloads necessary NLTK data.

</details>

---

## 🔧 **Setup Instructions**

1. **Clone the Repository**

   <details>
     <summary>Show commands</summary>

   ```bash
   git clone https://github.com/SullyGreene/TinyAGI.git
   cd TinyAGI
   ```
   </details>

2. **Set Up the Virtual Environment**

   Ensure Python 3.8+ is installed.

   <details>
     <summary>Show command</summary>

   ```bash
   python setup_env.py
   ```
   </details>

3. **Configure Environment Variables**

   Copy the example `.env` file and add your API keys.

   <details>
     <summary>Show commands</summary>

   ```bash
   cp .env.example .env
   ```
   </details>

4. **Run the Server**

   <details>
     <summary>Show command</summary>

   ```bash
   python run.py
   ```

   The server will be accessible at `http://localhost:5000`.

   </details>

---

## 🛠 **Usage**

### **Using the CLI**

Interact with TinyAGI through the command-line interface.

- **Generate Text**

   <details>
     <summary>Show command</summary>

   ```bash
   python -m TinyAGI.services.cli_manager generate --prompt "Tell me a joke."
   ```

   - **Options:**
       - `--prompt` or `-p`: The text prompt.
       - `--config` or `-c`: Path to a custom configuration file.
       - `--stream` or `-s`: Enable streaming output.

   </details>

### **Accessing the API**

- **Chat Endpoint**

   <details>
     <summary>Show command</summary>

   ```bash
   curl -X POST http://localhost:5000/chat \
        -H "Content-Type: application/json" \
        -d '{"messages": [{"role": "user", "content": "Hello!"}], "stream": false}'
   ```
   </details>

- **Generate Text Endpoint**

   <details>
     <summary>Show command</summary>

   ```bash
   curl -X POST http://localhost:5000/generate \
        -H "Content-Type: application/json" \
        -d '{"prompt": "Write a short story about a dragon.", "stream": false}'
   ```
   </details>

- **Embed Endpoint**

   <details>
     <summary>Show command</summary>

   ```bash
   curl -X POST http://localhost:5000/embed \
        -H "Content-Type: application/json" \
        -d '{"input": "Sample text for embedding."}'
   ```
   </details>

---

## 📚 **Documentation**

Access comprehensive documentation in the [`Documents/`](https://github.com/SullyGreene/TinyAGI/tree/main/Documents) directory.

---

## 🧪 **Testing**

Run TinyAGI tests to verify functionality.

### **Testing Ollama**

   <details>
     <summary>Show command</summary>

   ```bash
   python test_ollama.py
   ```

   - **Expected Output**:

      ```
      Response from OllamaAgent:
      The capital of France is Paris.
      ```

   - **Troubleshooting Tips**:
      - Ensure the Ollama server is running at `http://localhost:11434`.
      - Confirm correct API keys and authentication.

   </details>

---

## 📝 **Contributing**

Join the TinyAGI community by contributing your code, ideas, or feedback!

1. **Fork the Repository**

   <details>
     <summary>Show commands</summary>

   ```bash
   git checkout -b feature/YourFeatureName
   ```
   </details>

2. **Commit Your Changes**

   <details>
     <summary>Show command</summary>

   ```bash
   git commit -m "Add feature: YourFeatureName"
   ```
   </details>

3. **Push to Your Fork**

   <details>
     <summary>Show command</summary>

   ```bash
   git push origin feature/YourFeatureName
   ```
   </details>

4. **Submit a Pull Request**

---

## 🛡 **License**

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

---

## 📞 **Contact**

💬 **Get in Touch**

- **X (formerly Twitter)**: [@SullyGreene](https://twitter.com/SullyGreene)
- **GitHub**: [SullyGreene](https://github.com/SullyGreene)
- **PyPI**: [TinyAGI on PyPI](https://pypi.org/project/TinyAGI/)

---

## 🗺️ **Roadmap**

TinyAGI’s vision includes scaling to meet diverse AI needs. Here’s what’s planned:

<details>
  <summary>Phase 1: Core Enhancements 🚀</summary>

- **Agent Expansion**: Support additional agents and tools for specific domains.
- **Plugin Ecosystem**: Expand with plugins for data analysis, visual generation, and task-specific fine-tuning.
- **Advanced Error Handling**: Improve diagnostic logs and error handling.

</details>

<details>
  <summary>Phase 2: Advanced Task Orchestration 🤖</summary>

- **Multi-Agent Collaboration**: Enable agents to collaborate on complex tasks.
- **Task Scheduling & Automation**: Automate recurring actions and analysis.
- **Smart Prompting**: Dynamic prompt optimization for better task performance.

</details>

<details>
  <summary>Phase 3: Enhanced API and Developer Experience 🛠️</summary>

- **API V2**: Improve task queueing, agent behavior management, and access controls.
- **Interactive Documentation**: Launch an interactive portal with live code examples.
- **CLI Improvements**: Add user-friendly CLI commands.

</details>

<details>
  <summary>Phase 4: Ecosystem & Community Growth 🌍</summary>

- **Plugin Marketplace**: Set up a community-driven marketplace for plugins.
- **TinyAGI Hub**: A central hub for resources, tutorials, and community feedback.

</details>

<details>
  <summary>Phase 5: Scalability and Enterprise-Readiness 🏢</summary>

- **Distributed Agent Management**: Support for multi-server deployments.
- **Performance Optimization**: Improve resource use for concurrent agent management.
- **Enterprise Security**

: Enhanced data encryption and access control.

</details>

---

This structure makes each command, setup step, and roadmap phase easily expandable and hides them by default for a cleaner layout!
<details>
  <summary>## 🔧 Setup Instructions</summary>

1. **Clone the Repository**

    ```bash
    git clone https://github.com/SullyGreene/TinyAGI.git
    cd TinyAGI
    ```

2. **Set Up the Virtual Environment**

    Ensure Python 3.8+ is installed.

    ```bash
    python setup_env.py
    ```

3. **Configure Environment Variables**

    ```bash
    cp .env.example .env
    ```

    Add API keys in the `.env` file.

4. **Run the Server**

    ```bash
    python run.py
    ```

    Accessible at: `http://localhost:5000`

</details>

<details>
  <summary>## 🛠 Usage</summary>

### **Using the CLI**

Interact with TinyAGI right from your command line.

- **Generate Text**

    ```bash
    python -m TinyAGI.services.cli_manager generate --prompt "Tell me a joke."
    ```

    - **Options:**
        - `--prompt` or `-p`: The text prompt.
        - `--config` or `-c`: Path to a custom configuration.
        - `--stream` or `-s`: Enable streaming output.

### **Accessing the API**

- **Chat Endpoint**

    ```bash
    curl -X POST http://localhost:5000/chat \
         -H "Content-Type: application/json" \
         -d '{"messages": [{"role": "user", "content": "Hello!"}], "stream": false}'
    ```

- **Generate Text Endpoint**

    ```bash
    curl -X POST http://localhost:5000/generate \
         -H "Content-Type: application/json" \
         -d '{"prompt": "Write a short story about a dragon.", "stream": false}'
    ```

- **Embed Endpoint**

    ```bash
    curl -X POST http://localhost:5000/embed \
         -H "Content-Type: application/json" \
         -d '{"input": "Sample text for embedding."}'
    ```

</details>

<details>
  <summary>## 📚 Documentation</summary>

Explore full documentation for each TinyAGI component in the [`Documents/`](https://github.com/SullyGreene/TinyAGI/tree/main/Documents) directory.

```
Documents/
├── TinyAGI/
│   ├── __init__.md
│   ├── agent.md
│   ├── plugin_manager.md
│   ├── task_manager.md
│   └── utils.md
└── ...
```

Check out the [Documents Directory](https://github.com/SullyGreene/TinyAGI/tree/main/Documents) for in-depth guidance.

</details>

<details>
  <summary>## 🧪 Testing</summary>

Run TinyAGI tests to verify functionality.

- **Testing Ollama**

    ```bash
    python test_ollama.py
    ```

    - **Expected Output**:

        ```
        Response from OllamaAgent:
        The capital of France is Paris.
        ```

    - **Troubleshooting Tips**:
      - Ensure Ollama server is running at `http://localhost:11434`
      - Confirm correct API keys and authentication.

</details>

<details>
  <summary>## 📝 Contributing</summary>

Join the TinyAGI community by contributing your code, ideas, or feedback!

1. **Fork the Repository**
2. **Create a Branch**

    ```bash
    git checkout -b feature/YourFeatureName
    ```

3. **Commit Your Changes**

    ```bash
    git commit -m "Add feature: YourFeatureName"
    ```

4. **Push to Your Fork**

    ```bash
    git push origin feature/YourFeatureName
    ```

5. **Submit a Pull Request**

</details>

<details>
  <summary>## 🛡 License</summary>

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT).

</details>

<details>
  <summary>## 📞 Contact</summary>

💬 **Get in Touch**

- **X (formerly Twitter)**: [@SullyGreene](https://twitter.com/SullyGreene)
- **GitHub**: [SullyGreene](https://github.com/SullyGreene)
- **PyPI**: [TinyAGI on PyPI](https://pypi.org/project/TinyAGI/)

</details>

<details>
  <summary>## 🗺️ Roadmap</summary>

### **Phase 1: Core Enhancements** 🚀

- **Agent Expansion**: Introduce additional agent types, including GPT-4-based agents, language translators, and integrative tools for domain-specific tasks.
- **Plugin Ecosystem**: Expand with plugins for data analysis, visual generation, and task-specific fine-tuning.
- **Advanced Error Handling**: Granular error handling and diagnostic logging.

### **Phase 2: Advanced Task Orchestration** 🤖

- **Multi-Agent Collaboration**: Enable agents to collaborate on complex tasks, leveraging different models and plugins.
- **Task Scheduling & Automation**: Set up recurring actions, automated data analysis, and routine task execution.
- **Smart Prompting**: Introduce dynamic prompt optimization for better performance across language tasks.

### **Phase 3: Enhanced API and Developer Experience** 🛠️

- **API V2**: Develop a new API version with task queueing, agent behavior management, and improved access controls.
- **Interactive Documentation**: Set up an interactive portal with live examples and embedded code execution.
- **CLI Improvements**: Add more CLI commands and user-friendly prompts.

### **Phase 4: Ecosystem & Community Growth** 🌍

- **Plugin Marketplace**: Launch a TinyAGI Plugin Marketplace to share, review, and download plugins.
- **TinyAGI Hub**: A central resource hub for tutorials, demos, forums, and feature voting.

### **Phase 5: Scalability and Enterprise-Readiness** 🏢

- **Distributed Agent Management**: Support TinyAGI across multiple servers or cloud instances.
- **Performance Optimization**: Memory and CPU optimization for concurrent agent management.
- **Enterprise Security Features**: Add options for encrypted data

 storage, API key management, and access controls.

</details>

---
