#!/usr/bin/env python3
"""
Convert markdown recipes to Jekyll-compatible HTML files for GitHub Pages
Optimized for Samsung Food import compatibility
"""

import os
import yaml
import markdown
from pathlib import Path
import re
from datetime import datetime
import requests
import json
import time
from dotenv import load_dotenv
# Load environment variables from .env file
load_dotenv()


class RecipeConverter:
    def __init__(self, markdown_dir="_markdown", output_dir="_recipes", images_dir="assets/images"):
        self.markdown_dir = Path(markdown_dir)
        self.output_dir = Path(output_dir)
        self.images_dir = Path(images_dir)
        self.md = markdown.Markdown(extensions=['meta', 'tables', 'fenced_code'])
        self.deepinfra_api_key = os.getenv('DEEPINFRA_API_KEY')
        
    def ensure_directories(self):
        """Ensure required directories exist"""
        self.markdown_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)
        self.images_dir.mkdir(exist_ok=True)
        
    def parse_markdown_file(self, file_path):
        """Parse markdown file and extract frontmatter and content"""
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
            
        # Split frontmatter and content
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                frontmatter = yaml.safe_load(parts[1])
                content = parts[2].strip()
            else:
                frontmatter = {}
                content = content
        else:
            frontmatter = {}
            
        # Convert markdown to HTML
        html_content = self.md.convert(content)
        
        return frontmatter, html_content
        
    def create_jekyll_file(self, frontmatter, content, output_path):
        """Create Jekyll-compatible markdown file with frontmatter"""
        # Ensure required fields exist
        frontmatter.setdefault('title', 'Untitled Recipe')
        frontmatter.setdefault('description', '')
        frontmatter.setdefault('ingredients', [])
        frontmatter.setdefault('servings', 4)
        frontmatter.setdefault('prep_time', '15 min')
        frontmatter.setdefault('cook_time', '30 min')
        frontmatter.setdefault('difficulty', 'Medium')
        frontmatter.setdefault('tags', [])
        
        # Create Jekyll frontmatter
        jekyll_content = "---\n"
        jekyll_content += yaml.dump(frontmatter, default_flow_style=False, allow_unicode=True)
        jekyll_content += "---\n\n"
        jekyll_content += content
        
        # Write to file
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(jekyll_content)
            
    def convert_all(self):
        """Convert all markdown files in the directory"""
        self.ensure_directories()
        
        converted_recipes = []
        
        for md_file in self.markdown_dir.glob('*.md'):
            print(f"Converting {md_file.name}...")
            
            try:
                frontmatter, content = self.parse_markdown_file(md_file)
                
                # Create output filename
                base_name = md_file.stem
                output_file = self.output_dir / f"{base_name}.md"
                
                self.create_jekyll_file(frontmatter, content, output_file)
                print(f"✓ Created {output_file}")
                
                # Store recipe info for README update
                title = frontmatter.get('title', base_name.replace('-', ' ').title())
                converted_recipes.append({
                    'title': title,
                    'filename': base_name,
                    'frontmatter': frontmatter
                })
                
            except Exception as e:
                print(f"✗ Error processing {md_file}: {e}")
        
        # Update README with recipe links
        self.update_readme_links(converted_recipes)
        
    def update_readme_links(self, recipes):
        """Update README.md with links to converted recipes"""
        readme_path = Path('README.md')
        if not readme_path.exists():
            return
            
        with open(readme_path, 'r', encoding='utf-8') as f:
            readme_content = f.read()
        
        # Find the Available Recipes section
        if '## Available Recipes' not in readme_content:
            # Add Available Recipes section after Features
            features_end = readme_content.find('## Quick Start')
            if features_end != -1:
                recipes_section = "## Available Recipes\n\nHere are the recipes currently available in this collection:\n\n"
                
                for recipe in recipes:
                    url = f"https://ianmoran11.github.io/meals/recipes/{recipe['filename']}/"
                    image_url = f"https://ianmoran11.github.io/meals/assets/images/{recipe['filename']}.jpg"
                    recipes_section += f"- [{recipe['title']}]({url})\n"
                    if 'image' in recipe['frontmatter']:
                        recipes_section += f"  ![{recipe['title']}]({recipe['frontmatter']['image']})\n"
                
                recipes_section += "\n"
                readme_content = readme_content[:features_end] + recipes_section + readme_content[features_end:]
        
        else:
            # Update existing Available Recipes section
            start_idx = readme_content.find('## Available Recipes')
            end_idx = readme_content.find('## Quick Start', start_idx)
            
            if start_idx != -1 and end_idx != -1:
                recipes_section = "## Available Recipes\n\nHere are the recipes currently available in this collection:\n\n"
                
                for recipe in recipes:
                    url = f"https://ianmoran11.github.io/meals/recipes/{recipe['filename']}/"
                    recipes_section += f"- [{recipe['title']}]({url})\n"
                    if 'image' in recipe['frontmatter']:
                        recipes_section += f"  ![{recipe['title']}]({recipe['frontmatter']['image']})\n"
                
                recipes_section += "\n"
                readme_content = readme_content[:start_idx] + recipes_section + readme_content[end_idx:]
        
        with open(readme_path, 'w', encoding='utf-8') as f:
            f.write(readme_content)
        
        print("✓ Updated README.md with recipe links")

    def generate_recipe_image(self, recipe_title, recipe_description, recipe_ingredients):
        """Generate a recipe image using DeepInfra's image generation API"""
        if not self.deepinfra_api_key:
            print("⚠️  DEEPINFRA_API_KEY not found. Skipping image generation.")
            return None
            
        # Create a descriptive prompt for the image
        ingredients_text = ", ".join([ing.split()[0] if len(ing.split()) > 0 else ing for ing in recipe_ingredients[:5]])
        prompt = f"Professional food photography of {recipe_title}, featuring {ingredients_text}. High quality, appetizing presentation, natural lighting, restaurant style plating, 4K resolution"


        headers = {
            'Authorization': f'Bearer {self.deepinfra_api_key}',
            'Content-Type': 'application/json'
        }
        
        payload = {
            "model": "stabilityai/stable-diffusion-xl-base-1.0",
            "prompt": prompt,
            "negative_prompt": "blurry, low quality, distorted, unappetizing, text, watermark",
            "width": 1024,
            "height": 1024,
            "num_inference_steps": 30,
            "guidance_scale": 7.5
        }
        
        try:
            print(f"🎨 Generating image for: {recipe_title}")
            response = requests.post(
                "https://api.deepinfra.com/v1/inference/stabilityai/stable-diffusion-xl-base-1.0",
                headers=headers,
                json=payload,
                timeout=60
            )
            
            if response.status_code == 200:
                result = response.json()
                image_url = result.get('images', [None])[0]
                if image_url:
                    # Download and save the image
                    return self.download_image(image_url, recipe_title)
                else:
                    print(f"❌ No image URL in response for {recipe_title}")
                    return None
            else:
                print(f"❌ API error: {response.status_code} - {response.text}")
                return None
                
        except Exception as e:
            print(f"❌ Error generating image for {recipe_title}: {e}")
            return None
    
    def download_image(self, image_url, recipe_title):
        """Download and save the generated image"""
        try:
            response = requests.get(image_url, timeout=30)
            if response.status_code == 200:
                # Create filename from recipe title
                filename = recipe_title.lower().replace(' ', '-').replace('[^a-z0-9-]', '')
                image_path = self.images_dir / f"{filename}.jpg"
                
                # Save the image
                with open(image_path, 'wb') as f:
                    f.write(response.content)
                
                print(f"✓ Saved image: {image_path}")
                return f"/assets/images/{filename}.jpg"
            else:
                print(f"❌ Failed to download image: {response.status_code}")
                return None
                
        except Exception as e:
            print(f"❌ Error downloading image: {e}")
            return None

    def generate_images_for_recipes(self, recipes):
        """Generate images for all recipes"""
        if not self.deepinfra_api_key:
            print("⚠️  Set DEEPINFRA_API_KEY environment variable to enable image generation")
            return recipes
            
        updated_recipes = []
        for recipe in recipes:
            image_url = self.generate_recipe_image(
                recipe['title'],
                recipe['frontmatter'].get('description', ''),
                recipe['frontmatter'].get('ingredients', [])
            )
            
            if image_url:
                recipe['frontmatter']['image'] = image_url
                recipe['image'] = image_url
            
            updated_recipes.append(recipe)
            time.sleep(1)  # Rate limiting
        
        return updated_recipes
                
    def create_sample_recipe(self):
        """Create a sample markdown recipe for reference"""
        sample_recipe = """---
title: "Classic Chocolate Chip Cookies"
description: "Soft and chewy chocolate chip cookies that are perfect every time"
ingredients:
  - "2 1/4 cups all-purpose flour"
  - "1 tsp baking soda"
  - "1 tsp salt"
  - "1 cup butter, softened"
  - "3/4 cup granulated sugar"
  - "3/4 cup packed brown sugar"
  - "2 large eggs"
  - "2 tsp vanilla extract"
  - "2 cups chocolate chips"
servings: 24
prep_time: "15 min"
cook_time: "12 min"
difficulty: "Easy"
tags: ["dessert", "cookies", "chocolate", "baking"]
---

## Instructions

1. **Preheat** your oven to 375°F (190°C).

2. **Mix dry ingredients**: In a medium bowl, combine flour, baking soda, and salt. Set aside.

3. **Cream butter and sugars**: In a large bowl, beat softened butter, granulated sugar, and brown sugar until creamy.

4. **Add eggs and vanilla**: Beat in eggs one at a time, then add vanilla extract.

5. **Combine ingredients**: Gradually add the flour mixture to the wet ingredients, mixing until just combined.

6. **Add chocolate chips**: Fold in the chocolate chips.

7. **Form cookies**: Drop rounded tablespoons of dough onto ungreased baking sheets, spacing them 2 inches apart.

8. **Bake** for 9-11 minutes, or until golden brown around the edges.

9. **Cool** on the baking sheet for 2 minutes before transferring to a wire rack.

## Notes

- For softer cookies, slightly underbake them and let them finish cooking on the hot baking sheet.
- Store in an airtight container at room temperature for up to 1 week.
- Dough can be frozen for up to 3 months.
"""
        
        sample_file = self.markdown_dir / "sample-chocolate-chip-cookies.md"
        with open(sample_file, 'w', encoding='utf-8') as f:
            f.write(sample_recipe)
        print(f"✓ Created sample recipe: {sample_file}")

def main():
    converter = RecipeConverter()
    
    # Create sample recipe if no markdown files exist
    if not any(converter.markdown_dir.glob('*.md')):
        print("No markdown recipes found. Creating sample recipe...")
        converter.create_sample_recipe()
    
    # Convert all markdown files
    converter.convert_all()
    
    print("\nConversion complete!")
    print(f"Check the '{converter.output_dir}' directory for Jekyll-ready files.")

if __name__ == "__main__":
    main()
