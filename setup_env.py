# setup_env.py

import os
import sys
import subprocess
import logging
import platform
import json

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s %(levelname)s:%(message)s',
        handlers=[
            logging.StreamHandler(sys.stdout)
        ]
    )

def create_virtual_env(venv_path):
    import venv
    try:
        logging.info(f"Creating virtual environment at '{venv_path}'...")
        builder = venv.EnvBuilder(with_pip=True)
        builder.create(venv_path)
        logging.info("Virtual environment created successfully.")
    except Exception as e:
        logging.error(f"Failed to create virtual environment: {e}")
        sys.exit(1)

def install_requirements(venv_path, requirements_file):
    if not os.path.exists(requirements_file):
        logging.error(f"Requirements file '{requirements_file}' not found.")
        sys.exit(1)
    
    if platform.system() == 'Windows':
        pip_executable = os.path.join(venv_path, 'Scripts', 'pip.exe')
    else:
        pip_executable = os.path.join(venv_path, 'bin', 'pip')
    
    try:
        logging.info(f"Installing dependencies from '{requirements_file}'...")
        subprocess.check_call([pip_executable, 'install', '--upgrade', 'pip'])
        subprocess.check_call([pip_executable, 'install', '-r', requirements_file])
        logging.info("Dependencies installed successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to install dependencies: {e}")
        sys.exit(1)

def download_nltk_data(venv_path):
    try:
        if platform.system() == 'Windows':
            python_executable = os.path.join(venv_path, 'Scripts', 'python.exe')
        else:
            python_executable = os.path.join(venv_path, 'bin', 'python')
        
        logging.info("Downloading NLTK data...")
        subprocess.check_call([python_executable, '-m', 'nltk', 'download', 'punkt'])
        subprocess.check_call([python_executable, '-m', 'nltk', 'download', 'stopwords'])
        logging.info("NLTK data downloaded successfully.")
    except subprocess.CalledProcessError as e:
        logging.error(f"Failed to download NLTK data: {e}")
        sys.exit(1)

def main():
    setup_logging()
    
    project_root = os.path.dirname(os.path.abspath(__file__))
    venv_path = os.path.join(project_root, 'venv')
    requirements_file = os.path.join(project_root, 'TinyAGI/requirements.txt')
    
    if os.path.exists(venv_path):
        logging.info(f"Virtual environment already exists at '{venv_path}'. Skipping creation.")
    else:
        create_virtual_env(venv_path)
    
    install_requirements(venv_path, requirements_file)
    download_nltk_data(venv_path)
    
    logging.info("\nEnvironment setup is complete!")
    if platform.system() == 'Windows':
        activate_command = f"{venv_path}\\Scripts\\activate.bat"
    else:
        activate_command = f"source {venv_path}/bin/activate"
    
    logging.info(f"To activate the virtual environment, run:\n\n    {activate_command}\n")

if __name__ == '__main__':
    main()
