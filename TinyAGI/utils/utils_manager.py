import logging
from .json_utils import load_json
from .logging_utils import setup_logging
from .text_utils import sanitize_filename
from .nltk_utils import download_nltk_resources

class UtilsManager:
    """A centralized utility manager for handling JSON, logging, text sanitization, and NLTK resources."""

    def __init__(self):
        """Initialize the UtilsManager and set up logging."""
        setup_logging()

    def load_json(self, file_path):
        """Load a JSON file."""
        return load_json(file_path)

    def sanitize_filename(self, title):
        """Sanitize a filename."""
        return sanitize_filename(title)

    def download_nltk_resources(self):
        """Download NLTK resources."""
        download_nltk_resources()

# Example usage:
if __name__ == "__main__":
    utils_manager = UtilsManager()
    utils_manager.download_nltk_resources()