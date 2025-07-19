# Recipe Collection - GitHub Pages

A beautiful, searchable recipe collection designed for GitHub Pages and optimized for Samsung Food import.

## Features

- 📱 **Mobile-friendly** responsive design
- 🔍 **Search functionality** to quickly find recipes
- 📋 **Samsung Food compatible** - easily import recipes
- 🖨️ **Print-friendly** recipe pages
- 🏷️ **Categorized and tagged** for easy browsing
- 📊 **Schema markup** for better SEO and compatibility

## Quick Start

1. **Fork this repository** to your GitHub account
2. **Enable GitHub Pages** in repository settings
3. **Add your recipes** in the `_markdown/` directory
4. **Convert recipes** using the provided script
5. **Push to GitHub** - your site will be live!

## Adding Recipes

### Method 1: Using Markdown (Recommended)

1. Add your recipe as a markdown file in `_markdown/`
2. Use the provided format (see `_markdown/README.md`)
3. Run the conversion script:
   ```bash
   python scripts/convert-md-to-html.py
   ```


### Method 2: Direct Jekyll Files

1. Create files directly in `_recipes/` with Jekyll frontmatter
2. Follow the format shown in sample recipes

## Recipe Format

Each recipe should include:

```yaml
---
title: "Recipe Name"
description: "Brief description"
ingredients:
  - "2 cups flour"
  - "1 cup sugar"
servings: 4
prep_time: "15 min"
cook_time: "30 min"
difficulty: "Easy"
tags: ["dessert", "baking"]
---
```

## Samsung Food Import

To import recipes into Samsung Food:

1. Browse to any recipe on your GitHub Pages site
2. In Samsung Food, use the import feature
3. Paste the recipe URL
4. Samsung Food will automatically parse all details

## Local Development

1. Install dependencies:
   ```bash
   bundle install
   ```

2. Run locally:
   ```bash
   bundle exec jekyll serve
   ```

3. Visit `http://localhost:4000`

## Customization

- Edit `_config.yml` to change site settings
- Modify `assets/css/style.scss` for styling
- Update layouts in `_layouts/` for different page structures

## Contributing

1. Fork the repository
2. Create a feature branch
3. Add your recipes
4. Submit a pull request

## License

This project is open source and available under the [MIT License](LICENSE).
