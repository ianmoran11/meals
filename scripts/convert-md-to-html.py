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

class RecipeConverter:
    def __init__(self, markdown_dir="_markdown", output_dir="_recipes"):
        self.markdown_dir = Path(markdown_dir)
        self.output_dir = Path(output_dir)
        self.md = markdown.Markdown(extensions=['meta', 'tables', 'fenced_code'])
        
    def ensure_directories(self):
        """Ensure required directories exist"""
        self.markdown_dir.mkdir(exist_ok=True)
        self.output_dir.mkdir(exist_ok=True)
        
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
        
        for md_file in self.markdown_dir.glob('*.md'):
            print(f"Converting {md_file.name}...")
            
            try:
                frontmatter, content = self.parse_markdown_file(md_file)
                
                # Create output filename
                base_name = md_file.stem
                output_file = self.output_dir / f"{base_name}.md"
                
                self.create_jekyll_file(frontmatter, content, output_file)
                print(f"✓ Created {output_file}")
                
            except Exception as e:
                print(f"✗ Error processing {md_file}: {e}")
                
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
