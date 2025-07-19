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
