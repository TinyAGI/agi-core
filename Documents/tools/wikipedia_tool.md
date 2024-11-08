
# TinyAGI/tools/wikipedia_tool.py

## Overview

The `wikipedia_tool.py` file implements the `WikipediaTool` class, which interfaces with the Wikipedia API to fetch summaries and perform searches.

## Functionality

- **Language Support**: Configurable to fetch Wikipedia content in different languages.
- **Search**: Allows searching for Wikipedia pages based on a query.
- **Summary Retrieval**: Fetches concise summaries of specified Wikipedia pages.
- **Error Handling**: Manages disambiguation and page not found errors gracefully.

## Key Components

- **__init__**: Initializes the tool with language settings.
- **search**: Searches Wikipedia for a given query and returns page titles.
- **get_page_summary**: Retrieves a summary for a specified Wikipedia page.

## Usage

Instantiate the `WikipediaTool` with desired configurations and use its methods to interact with Wikipedia.

```python
from TinyAGI.tools.wikipedia_tool import WikipediaTool

config = {
    "language": "en"
}

wikipedia_tool = WikipediaTool(config)
search_results = wikipedia_tool.search("Artificial Intelligence", results=5)
summary = wikipedia_tool.get_page_summary("Artificial Intelligence")
```
