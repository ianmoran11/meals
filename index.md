## Recipe List
- [001 Mediterranean Greek Chicken Low Carb](/meals/recipes/001-mediterranean-greek-chicken-low-carb)
- [Recipe Name](/meals/recipes/README)
- [Avocado Toast with Low Carb Bread](/meals/recipes/avocado-toast-low-carb)
- [Simple Avocado on Toast](/meals/recipes/avocado-toast)
- [Flat White (Almond Milk)](/meals/recipes/flat-white-almond-milk)
- [Flat White](/meals/recipes/flat-white)
- [Greek Lemon Herb Roasted Chicken](/meals/recipes/greek-lemon-herb-roasted-chicken)
- [Simple Greek Salad](/meals/recipes/greek-salad)
- [Greek-Style Keto Chicken Souvlaki with Tzatziki](/meals/recipes/greek-style-keto-chicken-souvlaki-tzatziki)
- [Hommus and Carrots](/meals/recipes/hommus-carrots)
- [Keto Mediterranean Chicken Salad](/meals/recipes/keto-mediterranean-chicken-salad)
- [Keto Mediterranean Tuna Stuffed Avocados](/meals/recipes/keto-mediterranean-tuna-stuffed-avocados)
- [Mediterranean Baked Cod with Tomato-Olive Topping](/meals/recipes/mediterranean-baked-cod-tomato-olive-topping)
- [Mediterranean Cauliflower Rice Bowl with Grilled Shrimp](/meals/recipes/mediterranean-cauliflower-rice-bowl-grilled-shrimp)
- [Mediterranean Herb-Crusted Salmon with Roasted Vegetables](/meals/recipes/mediterranean-herb-crusted-salmon-roasted-vegetables)
- [Mediterranean Keto Stuffed Eggplant](/meals/recipes/mediterranean-keto-stuffed-eggplant)
- [Mediterranean Keto Zucchini Fritters](/meals/recipes/mediterranean-keto-zucchini-fritters)
- [Mediterranean Roasted Vegetable Medley](/meals/recipes/mediterranean-roasted-vegetable-medley)
- [Mediterranean Tandoori Chicken Tray Bake](/meals/recipes/mediterranean-tandoori-chicken-tray-bake)
- [Mediterranean Zucchini Lasagna](/meals/recipes/mediterranean-zucchini-lasagna)
- [Picolo Coffee (Almond Milk)](/meals/recipes/picolo-coffee-almond-milk)
- [Picolo Coffee](/meals/recipes/picolo-coffee)
- [Tuna Cheese Quesadilla with High Protein Wraps](/meals/recipes/tuna-cheese-quesadilla-high-protein)
- [Yogurt Berry Protein Smoothie](/meals/recipes/yogurt-berry-protein-smoothie)
## Features

- 📱 **Mobile-friendly** responsive design
- 🔍 **Search functionality** to quickly find recipes
- 📋 **Samsung Food compatible** - easily import recipes
- 🖨️ **Print-friendly** recipe pages
- 🏷️ **Categorized and tagged** for easy browsing
- 📊 **Schema markup** for better SEO and compatibility

## Available Recipes

{% for recipe in site.recipes %}
- [{{ recipe.title }}]({{ recipe.url | relative_url }})
{% endfor %}

- [001 Mediterranean Greek Chicken (Low Carb)]/_markdown/001-mediterranean-greek-chicken-low-carb.md
- [Avocado Toast]/_markdown/avocado-toast.md
- [Greek Lemon Herb Roasted Chicken]/_markdown/greek-lemon-herb-roasted-chicken.md
- [Greek Style Keto Chicken Souvlaki with Tzatziki]/_markdown/greek-style-keto-chicken-souvlaki-tzatziki.md
- [Keto Mediterranean Chicken Salad]/_markdown/keto-mediterranean-chicken-salad.md
- [Keto Mediterranean Tuna Stuffed Avocados]/_markdown/keto-mediterranean-tuna-stuffed-avocados.md
- [Mediterranean Baked Cod with Tomato Olive Topping]/_markdown/mediterranean-baked-cod-tomato-olive-topping.md
- [Mediterranean Cauliflower Rice Bowl with Grilled Shrimp]/_markdown/mediterranean-cauliflower-rice-bowl-grilled-shrimp.md
- [Mediterranean Herb Crusted Salmon with Roasted Vegetables]/_markdown/mediterranean-herb-crusted-salmon-roasted-vegetables.md
- [Mediterranean Keto Stuffed Eggplant]/_markdown/mediterranean-keto-stuffed-eggplant.md
- [Mediterranean Keto Zucchini Fritters]/_markdown/mediterranean-keto-zucchini-fritters.md
- [Mediterranean Roasted Vegetable Medley]/_markdown/mediterranean-roasted-vegetable-medley.md
- [Mediterranean Tandoori Chicken Tray Bake]/_markdown/mediterranean-tandoori-chicken-tray-bake.md
- [Mediterranean Zucchini Lasagna]/_markdown/mediterranean-zucchini-lasagna.md

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

## Repository URL
Your recipe collection will be available at: **https://ianmoran11.github.io/meals/**
