
# TinyAGI/services/cli_manager.py

## Overview

The `cli_manager.py` file provides a Command-Line Interface (CLI) for interacting with the TinyAGI framework. It allows users to perform tasks such as text generation directly from the terminal.

## Functionality

- **Command Parsing**: Utilizes the `argparse` library to parse command-line arguments and subcommands.
- **Text Generation**: Provides a `generate` command to create text based on user-provided prompts.
- **Streaming Support**: Allows users to receive streaming responses for real-time text generation.
- **Configuration Flexibility**: Supports specifying different configuration files for the agent system.

## Key Components

- **main**: Parses CLI arguments and executes the corresponding commands.
- **run_cli**: Entry point to run the CLI manager.

## Usage

Run the CLI manager to execute commands.

```bash
python -m TinyAGI.services.cli_manager generate --prompt "Hello, world!"
```

### Available Commands

- **generate**: Generate text based on a provided prompt.

    **Arguments**:
    
    - `--prompt` or `-p`: The prompt text for text generation.
    - `--config` or `-c`: (Optional) Path to a different configuration file.
    - `--stream` or `-s`: (Optional) Enable streaming of the generated text.

    **Example**:

    ```bash
    python -m TinyAGI.services.cli_manager generate --prompt "Write a short story about a dragon." --stream
    ```
