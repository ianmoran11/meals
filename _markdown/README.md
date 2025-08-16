# Markdown Recipe Format

This directory contains recipe files in markdown format. Each file should follow this structure:

## File Format

```markdown
---
title: "Recipe Name"
description: "Brief description of the recipe"
ingredients:
  - "1 cup flour"
  - "2 eggs"
  - "1/2 tsp salt"
servings: 4
prep_time: "15 min"
cook_time: "30 min"
difficulty: "Easy"
tags: ["tag1", "tag2", "category"]
---

## Instructions

1. First step
2. Second step
3. Continue with numbered steps...

## Notes

Any additional notes or tips go here.
```

## Recipe Collection

This directory contains 13 keto-friendly Mediterranean-style recipes.

### Chicken & Poultry

- [Greek Lemon Herb Roasted Chicken](greek-lemon-herb-roasted-chicken.md) - Tender, juicy roasted chicken with classic Mediterranean herbs and bright lemon flavor. A perfect low-carb main dish that's simple yet incredibly flavorful.
- [Greek-Style Keto Chicken Souvlaki with Tzatziki](greek-style-keto-chicken-souvlaki-tzatziki.md) - Tender marinated chicken skewers with authentic Greek flavors and creamy tzatziki sauce - perfect for keto
- [Keto Mediterranean Chicken Salad](keto-mediterranean-chicken-salad.md) - A fresh and protein-packed salad with grilled chicken, feta, olives, and a tangy lemon-herb dressing
- [Mediterranean Tandoori Chicken Tray Bake](mediterranean-tandoori-chicken-tray-bake.md) - An easy one-pan meal featuring low-carb Mediterranean vegetables and tandoori-spiced chicken - perfect for weeknight dinners

### Seafood

- [Keto Mediterranean Tuna Stuffed Avocados](keto-mediterranean-tuna-stuffed-avocados.md) - Creamy avocado halves filled with a Mediterranean-style tuna salad featuring olive oil, lemon, and fresh herbs
- [Mediterranean Baked Cod with Tomato-Olive Topping](mediterranean-baked-cod-tomato-olive-topping.md) - Flaky white cod fillets baked with a savory topping of tomatoes, olives, garlic, and Mediterranean herbs
- [Mediterranean Cauliflower Rice Bowl with Grilled Shrimp](mediterranean-cauliflower-rice-bowl-grilled-shrimp.md) - A fresh and flavorful keto bowl featuring seasoned cauliflower rice, grilled shrimp, and Mediterranean vegetables
- [Mediterranean Herb-Crusted Salmon with Roasted Vegetables](mediterranean-herb-crusted-salmon-roasted-vegetables.md) - A flavorful, keto-friendly salmon dish with a Mediterranean herb crust and low-carb roasted vegetables

### Meat

- [Mediterranean Keto Stuffed Eggplant](mediterranean-keto-stuffed-eggplant.md) - Tender roasted eggplant stuffed with a savory mixture of ground meat, herbs, and cheese - a satisfying keto meal

### Vegetarian

- [Mediterranean Keto Zucchini Fritters](mediterranean-keto-zucchini-fritters.md) - Crispy, golden fritters made with fresh zucchini, herbs, and feta cheese - perfect as a side dish or light meal
- [Mediterranean Roasted Vegetable Medley](mediterranean-roasted-vegetable-medley.md) - A colorful mix of roasted low-carb vegetables seasoned with Mediterranean herbs and olive oil
- [Mediterranean Zucchini Lasagna](mediterranean-zucchini-lasagna.md) - A low-carb lasagna using zucchini slices instead of pasta, layered with seasoned meat sauce and creamy cheese
- [Simple Avocado on Toast](avocado-toast.md) - Creamy avocado spread on perfectly toasted bread - Mediterranean style

### Recipe Stats

- **Total Recipes**: 13
- **Categories**: 4
- **Keto-Friendly**: 11 recipes
- **Mediterranean-Style**: 13 recipes


## Required Fields

- `title`: Recipe name
- `ingredients`: List of ingredients with measurements
- `servings`: Number of servings
- `prep_time`: Preparation time (e.g., "15 min", "1 hr")
- `cook_time`: Cooking time (e.g., "30 min", "1.5 hr")

## Optional Fields

- `description`: Brief recipe description
- `difficulty`: Easy, Medium, or Hard
- `tags`: List of tags for categorization
- `image`: URL to recipe image

## Usage

1. Add your markdown recipes to this directory
2. Run `python scripts/convert-md-to-html.py` to convert them to Jekyll format
3. The converted files will appear in `_recipes/` directory
