#!/usr/bin/env python3
"""
Example usage of the Dewey decimal-style topic tree implementation.
"""

import os
import xml.etree.ElementTree as ET
from dewey_tree import build_topic_tree, expand_to_include_topic, save_tree

def create_sample_tree():
    """Create and save a sample topic tree"""
    # You'll need to set your OpenRouter API key as an environment variable
    # export OPENROUTER_API_KEY="your-api-key-here"
    api_key = os.environ.get("OPENROUTER_API_KEY")
    
    if not api_key:
        print("Please set the OPENROUTER_API_KEY environment variable")
        print("Example: export OPENROUTER_API_KEY='your-api-key-here'")
        return
    
    # Build initial tree
    tree = build_topic_tree("Human Knowledge")
    
    # Expand tree to include specific topics
    topics = [
        "Machine Learning",
        "Ancient History",
        "Nutrition Science",
        "Classical Music"
    ]
    
    for topic in topics:
        print(f"\nExpanding tree to include: {topic}")
        success = expand_to_include_topic(tree, topic, api_key)
        
        if success:
            print(f"Successfully added '{topic}' to the tree")
        else:
            print(f"Failed to add '{topic}' to the tree")
    
    # Save the final tree
    save_tree(tree, "kt.xml")
    print("\nFinal tree saved to kt.xml")
    
    # Display a simplified view of the tree
    print("\nTree structure:")
    display_tree(tree)

def display_tree(tree: ET.Element, level: int = 0):
    """Display a simplified view of the tree structure"""
    indent = "  " * level
    if hasattr(tree, 'tag') and tree.tag == 'topic_tree':
        print(f"{indent}<topic_tree>")
        for child in tree:
            display_tree(child, level + 1)
    elif hasattr(tree, 'tag') and tree.tag == 'topic':
        topic_id = tree.get('id', 'unknown')
        topic_text = tree.text.strip() if tree.text else ""
        print(f"{indent}<topic id='{topic_id}'>{topic_text}</topic>")
        for child in tree:
            if child.tag == 'topic':
                display_tree(child, level + 1)

if __name__ == "__main__":
    create_sample_tree()
