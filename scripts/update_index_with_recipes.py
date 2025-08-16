import os
import re

def extract_title_from_md(file_path):
    """Extracts the title from the YAML front matter of a markdown file."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            for line in f:
                if line.startswith('title: '):
                    # Extract title value, handling quotes
                    title_match = re.search(r'title:\s*"?(.*?)"?\s*$', line)
                    if title_match:
                        return title_match.group(1).strip()
    except FileNotFoundError:
        print(f"Warning: File not found {file_path}")
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
    return None

def generate_recipe_links(markdown_dir):
    """Generates a list of markdown links for recipes in the given directory."""
    recipe_links = []
    if not os.path.isdir(markdown_dir):
        print(f"Error: Directory not found {markdown_dir}")
        return ""

    for filename in sorted(os.listdir(markdown_dir)):
        if filename.endswith(".md"):
            file_path = os.path.join(markdown_dir, filename)
            title = extract_title_from_md(file_path)
            if title:
                # Create a user-friendly link
                # New format: /meals/recipes/filename (without .md)
                link_filename = filename.replace(".md", "")
                link = f"- [{title}](/meals/recipes/{link_filename})"
                recipe_links.append(link)
            else:
                # Fallback to filename if title not found
                fallback_title = filename.replace(".md", "").replace("-", " ").title()
                link_filename = filename.replace(".md", "")
                link = f"- [{fallback_title}](/meals/recipes/{link_filename})"
                recipe_links.append(link)
                print(f"Warning: Could not extract title from {file_path}, using fallback.")
    return "\n".join(recipe_links)

def update_index_md(index_path, recipe_links_md, section_heading):
    """Updates the index.md file with the new recipe links."""
    if not os.path.isfile(index_path):
        print(f"Error: Index file not found {index_path}")
        return

    try:
        with open(index_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"Error reading index file {index_path}: {e}")
        return

    # Pattern to find the section and its content
    # It looks for the heading, then captures everything until the next ## heading or end of file
    section_pattern = re.compile(
        rf"^{re.escape(section_heading)}\s*\n(.*?)(?=^##|\Z)",
        re.MULTILINE | re.DOTALL
    )

    new_section_content = f"{section_heading}\n{recipe_links_md}\n"

    if section_pattern.search(content):
        # Replace existing section
        updated_content = section_pattern.sub(new_section_content, content)
        print(f"Updated existing '{section_heading}' section in {index_path}.")
    else:
        # Add new section at the top of the file
        updated_content = f"{new_section_content}\n{content}"
        print(f"Added new '{section_heading}' section to the top of {index_path}.")

    try:
        with open(index_path, 'w', encoding='utf-8') as f:
            f.write(updated_content)
        print(f"Successfully wrote updated content to {index_path}")
    except Exception as e:
        print(f"Error writing to index file {index_path}: {e}")

if __name__ == "__main__":
    markdown_directory = "_markdown"
    index_file_path = "index.md"
    recipe_list_heading = "## Recipe List"

    print(f"Generating recipe links from '{markdown_directory}'...")
    recipe_links = generate_recipe_links(markdown_directory)

    if recipe_links:
        print(f"\nGenerated Recipe Links:\n{recipe_links}\n")
        print(f"Updating '{index_file_path}'...")
        update_index_md(index_file_path, recipe_links, recipe_list_heading)
        print("Script finished.")
    else:
        print("No recipe links were generated. Index file not updated.")
