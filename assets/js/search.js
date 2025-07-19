// Simple search functionality
document.addEventListener('DOMContentLoaded', function() {
    const searchInput = document.getElementById('search-input');
    const searchResults = document.getElementById('search-results');
    
    if (!searchInput || !searchResults) return;
    
    // Get all recipes
    const recipes = [];
    {% for recipe in site.recipes %}
    recipes.push({
        title: "{{ recipe.title | escape }}",
        description: "{{ recipe.description | escape }}",
        url: "{{ recipe.url | relative_url }}",
        tags: [{% for tag in recipe.tags %}"{{ tag }}"{% unless forloop.last %},{% endunless %}{% endfor %}]
    });
    {% endfor %}
    
    searchInput.addEventListener('input', function(e) {
        const query = e.target.value.toLowerCase().trim();
        
        if (query.length < 2) {
            searchResults.innerHTML = '';
            searchResults.style.display = 'none';
            return;
        }
        
        const filteredRecipes = recipes.filter(recipe => 
            recipe.title.toLowerCase().includes(query) ||
            recipe.description.toLowerCase().includes(query) ||
            recipe.tags.some(tag => tag.toLowerCase().includes(query))
        );
        
        displayResults(filteredRecipes);
    });
    
    function displayResults(results) {
        searchResults.innerHTML = '';
        
        if (results.length === 0) {
            searchResults.innerHTML = '<div class="search-result">No recipes found</div>';
        } else {
            results.forEach(recipe => {
                const div = document.createElement('div');
                div.className = 'search-result';
                div.innerHTML = `
                    <strong>${recipe.title}</strong>
                    <p>${recipe.description.substring(0, 100)}...</p>
                `;
                div.addEventListener('click', () => {
                    window.location.href = recipe.url;
                });
                searchResults.appendChild(div);
            });
        }
        
        searchResults.style.display = 'block';
    }
    
    // Close search results when clicking outside
    document.addEventListener('click', function(e) {
        if (!e.target.closest('.search-container')) {
            searchResults.style.display = 'none';
        }
    });
});
