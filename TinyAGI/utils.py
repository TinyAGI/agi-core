# MIT License
# Copyright (c) 2024 Sully Greene
# Repository: https://github.com/SullyGreene
# Profile: https://x.com/@SullyGreene

# TinyAGI/utils.py

import json
import re
import nltk
import os
import logging
from dotenv import load_dotenv

class Utils:
    """Utility class for common operations such as logging, JSON loading, and text processing."""

    def __init__(self):
        """Initialize utilities and configure logging."""
        load_dotenv()
        self.setup_logging()

    def setup_logging(self):
        """
        Configure the logging settings.
        """
        log_level = os.getenv('LOG_LEVEL', 'INFO').upper()
        logging.basicConfig(
            level=getattr(logging, log_level, logging.INFO),
            format='%(asctime)s %(levelname)s:%(name)s:%(message)s',
            handlers=[logging.StreamHandler()]
        )
        logging.info("Logging configured successfully.")

    def load_json(self, file_path):
        """
        Load JSON data from a file.

        :param file_path: Path to the JSON file.
        :return: Dictionary containing JSON data.
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                data = json.load(f)
            logging.info(f"Loaded JSON data from '{file_path}'.")
            return data
        except FileNotFoundError:
            logging.error(f"JSON file not found at '{file_path}'.")
            return {}
        except json.JSONDecodeError as e:
            logging.error(f"Error decoding JSON from '{file_path}': {e}")
            return {}
        except Exception as e:
            logging.error(f"Error loading JSON from '{file_path}': {e}")
            return {}

    def sanitize_filename(self, title):
        """
        Sanitize a string to be used as a safe filename.

        :param title: Original string.
        :return: Sanitized string.
        """
        sanitized = re.sub(r'\W+', '_', title.lower()).strip('_')
        logging.debug(f"Sanitized filename: Original='{title}', Sanitized='{sanitized}'")
        return sanitized

    def download_nltk_resources(self):
        """
        Ensure NLTK resources are available.
        """
        try:
            nltk.download('punkt', quiet=True)
            nltk.download('stopwords', quiet=True)
            logging.info("NLTK resources downloaded successfully.")
        except Exception as e:
            logging.error(f"Error downloading NLTK resources: {e}")

# Example usage:
if __name__ == "__main__":
    utils = Utils()
    utils.download_nltk_resources()