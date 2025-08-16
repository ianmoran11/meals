#!/usr/bin/env python3
"""
Script to update the _markdown/README.md file with links to all recipe files.
"""

import os
import re
from pathlib import Path

def extract_recipe_info(filepath):
    """Extract title and description from a recipe markdown file."""
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Extract frontmatter
    frontmatter_match = re.search(r'^---\n(.*?)\n---', content, re.DOTALL | re.MULTILINE)
    if not frontmatter_match:
        return None, None, []
    
    frontmatter = frontmatter_match.group(1)
    
    # Extract title
    title_match = re.search(r'^title:\s*"([^"]+)"', frontmatter, re.MULTILINE)
    title = title_match.group(1) if title_match else None
    
    # Extract description
    desc_match = re.search(r'^description:\s*"([^"]+)"', frontmatter, re.MULTILINE)
    description = desc_match.group(1) if desc_match else None
    
    # Extract tags
    tags_match = re.search(r'^tags:\s*\[(.*?)\]', frontmatter, re.MULTILINE)
    tags = []
    if tags_match:
        tags_str = tags_match.group(1)
        tags = [tag.strip().strip('"') for tag in tags_str.split(',')]
    
    return title, description, tags

def categorize_recipes(recipes):
    """Categorize recipes based on their tags and content."""
    categories = {
        'Chicken & Poultry': [],
        'Seafood': [],
        'Meat': [],
        'Vegetarian': [],
        'Salads & Bowls': [],
        'Other': []
    }
    
    for recipe in recipes:
        filename, title, description, tags = recipe
        tags_lower = [tag.lower() for tag in tags]
        
        # Categorize based on tags and title
        if any(tag in tags_lower for tag in ['chicken', 'poultry']):
            categories['Chicken & Poultry'].append(recipe)
        elif any(tag in tags_lower for tag in ['seafood', 'fish', 'salmon', 'cod', 'shrimp', 'tuna']):
            categories['Seafood'].append(recipe)
        elif any(tag in tags_lower for tag in ['lamb', 'beef', 'meat']) and 'chicken' not in tags_lower:
            categories['Meat'].append(recipe)
        elif any(tag in tags_lower for tag in ['vegetarian', 'vegetables', 'fritters']):
            categories['Vegetarian'].append(recipe)
        elif any(tag in tags_lower for tag in ['salad', 'bowl']):
            categories['Salads & Bowls'].append(recipe)
        else:
            # Check title for categorization
            title_lower = title.lower() if title else ''
            if 'chicken' in title_lower:
                categories['Chicken & Poultry'].append(recipe)
            elif any(word in title_lower for word in ['salmon', 'cod', 'shrimp', 'tuna', 'fish']):
                categories['Seafood'].append(recipe)
            elif any(word in title_lower for word in ['lamb', 'beef']):
                categories['Meat'].append(recipe)
            elif 'salad' in title_lower or 'bowl' in title_lower:
                categories['Salads & Bowls'].append(recipe)
            elif 'vegetable' in title_lower or 'zucchini' in title_lower or 'eggplant' in title_lower:
                categories['Vegetarian'].append(recipe)
            else:
                categories['Other'].append(recipe)
    
    # Remove empty categories
    return {k: v for k, v in categories.items() if v}

def update_readme():
    """Update the README.md file with links to all recipes."""
    markdown_dir = Path('_markdown')
    readme_path = markdown_dir / 'README.md'
    
    # Get all markdown files (excluding README)
    recipe_files = [f for f in markdown_dir.glob('*.md') if f.name != 'README.md']
    recipe_files.sort()
    
    # Extract recipe information
    recipes = []
    for filepath in recipe_files:
        title, description, tags = extract_recipe_info(filepath)
        if title:
            recipes.append((filepath.name, title, description, tags))
    
    # Categorize recipes
    categorized = categorize_recipes(recipes)
    
    # Read current README content
    with open(readme_path, 'r', encoding='utf-8') as f:
        readme_content = f.read()
    
    # Find where to insert the recipe list (before ## Required Fields or at the end)
    insert_marker = '## Required Fields'
    if insert_marker in readme_content:
        parts = readme_content.split(insert_marker)
        before_section = parts[0].rstrip()
        after_section = insert_marker + parts[1]
    else:
        before_section = readme_content.rstrip()
        after_section = ''
    
    # Remove any existing recipe list section
    if '## Recipe Collection' in before_section:
        before_section = before_section.split('## Recipe Collection')[0].rstrip()
    
    # Build the new recipe list section
    recipe_section = '\n\n## Recipe Collection\n\n'
    recipe_section += f'This directory contains {len(recipes)} keto-friendly Mediterranean-style recipes.\n\n'
    
    # Add categorized recipes
    for category, category_recipes in categorized.items():
        if category_recipes:
            recipe_section += f'### {category}\n\n'
            for filename, title, description, tags in sorted(category_recipes, key=lambda x: x[1]):
                recipe_section += f'- [{title}]({filename})'
                if description:
                    recipe_section += f' - {description}'
                recipe_section += '\n'
            recipe_section += '\n'
    
    # Add quick stats
    recipe_section += '### Recipe Stats\n\n'
    recipe_section += f'- **Total Recipes**: {len(recipes)}\n'
    recipe_section += f'- **Categories**: {len(categorized)}\n'
    
    # Count keto recipes
    keto_count = sum(1 for r in recipes if 'keto' in [tag.lower() for tag in r[3]])
    if keto_count > 0:
        recipe_section += f'- **Keto-Friendly**: {keto_count} recipes\n'
    
    # Count mediterranean recipes
    med_count = sum(1 for r in recipes if 'mediterranean' in [tag.lower() for tag in r[3]])
    if med_count > 0:
        recipe_section += f'- **Mediterranean-Style**: {med_count} recipes\n'
    
    recipe_section += '\n'
    
    # Combine all parts
    new_content = before_section + recipe_section + '\n' + after_section
    
    # Write updated README
    with open(readme_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    print(f"✅ Updated {readme_path} with {len(recipes)} recipes in {len(categorized)} categories")
    for category, category_recipes in categorized.items():
        print(f"   - {category}: {len(category_recipes)} recipes")

if __name__ == '__main__':
    # Change to the project root directory
    script_dir = Path(__file__).parent
    project_root = script_dir.parent
    os.chdir(project_root)
    
    update_readme()
