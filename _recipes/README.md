---
cook_time: 30 min
description: ''
difficulty: Medium
ingredients: []
prep_time: 15 min
servings: 4
tags: []
title: Untitled Recipe
---

<h1>Markdown Recipe Format</h1>
<p>This directory contains recipe files in markdown format. Each file should follow this structure:</p>
<h2>File Format</h2>
<pre><code class="language-markdown">---
title: &quot;Recipe Name&quot;
description: &quot;Brief description of the recipe&quot;
ingredients:
  - &quot;1 cup flour&quot;
  - &quot;2 eggs&quot;
  - &quot;1/2 tsp salt&quot;
servings: 4
prep_time: &quot;15 min&quot;
cook_time: &quot;30 min&quot;
difficulty: &quot;Easy&quot;
tags: [&quot;tag1&quot;, &quot;tag2&quot;, &quot;category&quot;]
---

## Instructions

1. First step
2. Second step
3. Continue with numbered steps...

## Notes

Any additional notes or tips go here.
</code></pre>
<h2>Required Fields</h2>
<ul>
<li><code>title</code>: Recipe name</li>
<li><code>ingredients</code>: List of ingredients with measurements</li>
<li><code>servings</code>: Number of servings</li>
<li><code>prep_time</code>: Preparation time (e.g., "15 min", "1 hr")</li>
<li><code>cook_time</code>: Cooking time (e.g., "30 min", "1.5 hr")</li>
</ul>
<h2>Optional Fields</h2>
<ul>
<li><code>description</code>: Brief recipe description</li>
<li><code>difficulty</code>: Easy, Medium, or Hard</li>
<li><code>tags</code>: List of tags for categorization</li>
<li><code>image</code>: URL to recipe image</li>
</ul>
<h2>Usage</h2>
<ol>
<li>Add your markdown recipes to this directory</li>
<li>Run <code>python scripts/convert-md-to-html.py</code> to convert them to Jekyll format</li>
<li>The converted files will appear in <code>_recipes/</code> directory</li>
</ol>