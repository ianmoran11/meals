## Available Recipes
Here are the recipes currently available in this collection:
- [Greek Lemon Herb Roasted Chicken](https://ianmoran11.github.io/meals/recipes/greek-lemon-herb-roasted-chicken/)
- [Classic Chocolate Chip Cookies](https://ianmoran11.github.io/meals/recipes/sample-chocolate-chip-cookies/)

## Adding Recipes
### Method 1: Using Markdown (Recommended)
1. Add your recipe as a markdown file in `_markdown/`
2. Use the provided format (see `_markdown/README.md`)
3. Run the conversion script:
   ```bash
   python scripts/convert-md-to-html.py
   ```
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
