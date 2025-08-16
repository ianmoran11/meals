# Dewey Decimal-Style Topic Tree

This Python implementation creates a hierarchical topic tree using an XML structure inspired by the Dewey Decimal System. Each branch can have up to 26 leaves, represented by letters A-Z.

## Features

- Creates an XML-based hierarchical topic tree
- Uses OpenRouter API for semantic topic categorization
- Recursively expands the tree to include specific topics
- Limits each branch to 26 children (A-Z)
- Saves the tree structure to an XML file

## Requirements

- Python 3.6+
- OpenRouter API key

## Installation

1. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

2. Set your OpenRouter API key as an environment variable:
   ```bash
   export OPENROUTER_API_KEY="your-api-key-here"
   ```

## Usage

### Basic Usage

```python
import os
from dewey_tree import build_topic_tree, expand_to_include_topic, save_tree

# Set your API key
api_key = os.environ.get("OPENROUTER_API_KEY")

# Build initial tree
tree = build_topic_tree("General Knowledge")

# Expand tree to include a specific topic
expand_to_include_topic(tree, "Quantum Computing", api_key)

# Save the tree to an XML file
save_tree(tree, "kt.xml")
```

### Example Script

Run the example script to see how it works:
```bash
python example_usage.py
```

This will create a tree with several sample topics and save it to `kt.xml`.

## How It Works

1. The system starts with a root topic (default: "General Knowledge")
2. When expanding to include a new topic:
   - It finds the most relevant existing node using semantic similarity
   - Queries OpenRouter for up to 26 subtopics of that node
   - Adds the subtopics as children (labeled A-Z)
   - Recursively continues until the target topic is included
3. Each expansion is limited to 26 children per node
4. The tree is saved as an XML file with the following structure:

```xml
<topic_tree>
  <topic id="root">General Knowledge</topic>
    <topic id="A">Science</topic>
      <topic id="A.A">Physics</topic>
        <topic id="A.A.A">Quantum Mechanics</topic>
      </topic>
    </topic>
  </topic>
</topic_tree>
```

## API Reference

### `build_topic_tree(root_topic: str = "General Knowledge") -> ET.Element`
Creates a new topic tree with the specified root topic.

### `expand_to_include_topic(tree: ET.Element, target_topic: str, api_key: str, max_depth: int = 10) -> bool`
Recursively expands the tree until it includes the target topic. Returns `True` on success, `False` on failure.

### `save_tree(tree: ET.Element, filename: str = "kt.xml")`
Saves the topic tree to an XML file.

## Model Used

This implementation uses the `qwen/qwen3-235b-a22b-thinking-2507` model from OpenRouter for semantic topic categorization.
