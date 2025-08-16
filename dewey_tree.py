import xml.etree.ElementTree as ET
import requests
import os

def build_topic_tree(root_topic: str = "General Knowledge") -> ET.Element:
    """Initialize XML tree with root topic"""
    tree = ET.Element('topic_tree')
    root = ET.SubElement(tree, 'topic', id='root')
    root.text = root_topic
    return tree

def _query_openrouter(api_key: str, prompt: str) -> str:
    """Query OpenRouter API with given prompt"""
    url = "https://openrouter.ai/api/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {api_key}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "qwen/qwen3-235b-a22b-thinking-2507",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    try:
        response = requests.post(url, headers=headers, json=data)
        response.raise_for_status()
        return response.json()['choices'][0]['message']['content'].strip()
    except Exception as e:
        print(f"Error querying OpenRouter: {e}")
        return ""

def _get_relevant_subtopics(parent_topic: str, target_topic: str, api_key: str) -> list:
    """Query OpenRouter for relevant subtopics"""
    prompt = f"""List up to 26 subtopics under "{parent_topic}" that could contain "{target_topic}".
If there are more than 26 relevant subtopics, provide broader categories to stay within limit.
Return ONLY the subtopic names, one per line in sentence case.
Example response:
Physics
Chemistry
Biology"""
    
    response = _query_openrouter(api_key, prompt)
    return [line.strip() for line in response.split('\n') if line.strip()][:26]

def _is_topic_covered(node_text: str, target: str, api_key: str) -> bool:
    """Check if a topic semantically covers the target topic"""
    prompt = f"Does the topic '{node_text}' semantically cover '{target}'? Answer YES or NO."
    response = _query_openrouter(api_key, prompt)
    return "YES" in response.upper()

def _find_deepest_relevant_node(tree: ET.Element, target_topic: str, api_key: str) -> ET.Element:
    """Find the deepest node that is relevant to the target topic"""
    def _search(node: ET.Element) -> ET.Element:
        # Check if any children are relevant
        for child in node:
            if _is_topic_covered(child.text.strip(), target_topic, api_key):
                return _search(child)  # Go deeper
        return node  # No relevant children, return current node
    
    # Start from root
    root = tree.find('.//topic[@id="root"]')
    if root is None:
        root = tree  # Fallback to tree itself
    return _search(root)

def _select_most_relevant_child(node: ET.Element, target_topic: str, api_key: str) -> ET.Element:
    """Select the most relevant child node based on semantic similarity"""
    best_child = None
    best_score = -1
    
    for child in node:
        prompt = f"On a scale of 1-10, how relevant is '{child.text.strip()}' to '{target_topic}'? Return only the number."
        response = _query_openrouter(api_key, prompt)
        try:
            score = int(response)
            if score > best_score:
                best_score = score
                best_child = child
        except ValueError:
            # If we can't parse the score, we'll just use the first child
            if best_child is None:
                best_child = child
    
    return best_child if best_child is not None else node[0] if len(node) > 0 else node

def expand_to_include_topic(
    tree: ET.Element, 
    target_topic: str,
    api_key: str,
    max_depth: int = 10
) -> bool:
    """Recursively expand tree until target topic is included"""
    current_node = _find_deepest_relevant_node(tree, target_topic, api_key)
    depth = 0
    
    while not _is_topic_covered(current_node.text.strip() if current_node.text else "", target_topic, api_key) and depth < max_depth:
        # Get subtopics from OpenRouter
        subtopics = _get_relevant_subtopics(
            current_node.text.strip() if current_node.text else "General",
            target_topic,
            api_key
        )
        
        if not subtopics:
            print(f"Failed to get subtopics for '{current_node.text}'. Aborting.")
            return False  # Abort per requirements
        
        # Clear existing children (if any) and add new subtopics as children (A-Z)
        current_node.clear()
        # Restore the text content
        current_node.text = current_node.text
        
        # Add subtopics as children (A-Z)
        for i, subtopic in enumerate(subtopics[:26]):
            letter = chr(65 + i)  # A-Z
            node_id = f"{current_node.get('id')}.{letter}" if current_node.get('id') != 'root' else letter
            child = ET.SubElement(current_node, 'topic', id=node_id)
            child.text = subtopic
        
        # Find most relevant child for next iteration
        current_node = _select_most_relevant_child(current_node, target_topic, api_key)
        if current_node is None or current_node == node:
            print("Could not find a relevant child node. Aborting.")
            return False
            
        depth += 1
    
    return True

def save_tree(tree: ET.Element, filename: str = "kt.xml"):
    """Save XML tree to file"""
    # Create a new tree with proper XML declaration
    tree_xml = ET.ElementTree(tree)
    tree_xml.write(filename, encoding='utf-8', xml_declaration=True)
    print(f"Tree saved to {filename}")

def main():
    """Main function to demonstrate the topic tree functionality"""
    # Get API key from environment variable
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Please set OPENROUTER_API_KEY environment variable")
        return
    
    # Build initial tree
    tree = build_topic_tree("General Knowledge")
    
    # Example: Expand tree to include "Quantum Computing"
    target = "Quantum Computing"
    print(f"Expanding tree to include: {target}")
    
    success = expand_to_include_topic(tree, target, api_key)
    
    if success:
        print("Tree successfully expanded")
        save_tree(tree)
    else:
        print("Failed to expand tree to include target topic")

if __name__ == "__main__":
    main()
