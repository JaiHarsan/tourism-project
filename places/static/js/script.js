/* ========== DOM ELEMENTS ========== */
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const placesContainer = document.getElementById('placesContainer');
const emptyState = document.getElementById('emptyState');
const themeToggle = document.getElementById('themeToggle');
const filterBtns = document.querySelectorAll('.filter-btn:not(.city-filter)');

let currentFilter = 'all';
let currentSearch = '';
let isSearching = false;

/* ========== HANDLE SEARCH ========== */
function handleSearch() {
    if (searchInput && !isSearching) {
        currentSearch = searchInput.value.toLowerCase().trim();
        fetchPlacesFromAPI();
        updateClearButton();
    }
    return false;
}

/* ========== CLEAR SEARCH ========== */
function clearSearch() {
    if (searchInput) {
        searchInput.value = '';
        currentSearch = '';
        updateClearButton();
        fetchPlacesFromAPI();
        searchInput.focus();
    }
    return false;
}

/* ========== UPDATE CLEAR BUTTON VISIBILITY ========== */
function updateClearButton() {
    const clearBtn = document.getElementById('clearSearchBtn');
    if (clearBtn) {
        clearBtn.style.display = (searchInput && searchInput.value.trim()) ? 'flex' : 'none';
    }
}

/* ========== INITIALIZE ========== */
document.addEventListener('DOMContentLoaded', () => {
    // Prevent any form submission on search container
    document.querySelectorAll('.search-container').forEach(container => {
        container.addEventListener('submit', (e) => {
            e.preventDefault();
            return false;
        });
    });

    // Add event listeners to filter buttons
    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const filter = btn.getAttribute('data-filter');
            filterCategory(filter);
        });
    });

    // Search functionality - trigger on Enter key
    if (searchInput) {
        searchInput.addEventListener('keydown', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                e.stopPropagation();
                handleSearch();
                return false;
            }
        });
        
        searchInput.addEventListener('keypress', (e) => {
            if (e.key === 'Enter') {
                e.preventDefault();
                e.stopPropagation();
                return false;
            }
        });
        
        // Show/hide clear button as user types
        searchInput.addEventListener('input', (e) => {
            updateClearButton();
        });
    }

    // Search button click
    if (searchBtn) {
        searchBtn.addEventListener('click', (e) => {
            e.preventDefault();
            e.stopPropagation();
            handleSearch();
            return false;
        });
    }

    // Theme toggle
    if (themeToggle) {
        themeToggle.addEventListener('click', toggleTheme);
    }

    // Set first button as active
    if (filterBtns.length > 0) {
        filterBtns[0].classList.add('active');
    }

    // Load initial places
    fetchPlacesFromAPI();
});

/* ========== FETCH PLACES FROM API ========== */
async function fetchPlacesFromAPI() {
    try {
        isSearching = true;
        
        // Build query parameters for general search API
        let params = new URLSearchParams();
        
        if (currentFilter !== 'all') {
            params.append('category', currentFilter);
        }
        
        if (currentSearch) {
            params.append('q', currentSearch);
        }

        // Fetch from general search API (all places from all cities)
        const response = await fetch(`/api/search/?${params.toString()}`);
        
        if (!response.ok) {
            throw new Error('API request failed');
        }
        
        const data = await response.json();

        // Render the places (handle both 'results' and 'places' response formats)
        const placesData = data.results || data.places || [];
        renderPlaces(placesData);
        
        isSearching = false;
    } catch (error) {
        console.error('Error fetching places:', error);
        isSearching = false;
        if (placesContainer) {
            placesContainer.innerHTML = '<p style="text-align: center; color: var(--text-light);">Error loading places. Please try again.</p>';
        }
    }
}

/* ========== RENDER PLACES FROM API DATA ========== */
function renderPlaces(places) {
    if (!placesContainer) return;

    // Clear container
    placesContainer.innerHTML = '';

    if (places.length === 0) {
        // Show empty state
        if (emptyState) {
            emptyState.style.display = 'block';
        }
        return;
    }

    // Hide empty state
    if (emptyState) {
        emptyState.style.display = 'none';
    }

    // Render each place
    places.forEach(place => {
        // Format category name for display
        const categoryDisplay = place.category === 'hidden_spots' ? 'Hidden Spots' : 
                               place.category === 'falls' ? 'Waterfalls' :
                               place.category.charAt(0).toUpperCase() + place.category.slice(1);
        
        // Format city name for display
        const cityDisplay = place.city.charAt(0).toUpperCase() + place.city.slice(1);
        
        // Image handling - use actual image or placeholder
        const imageContent = place.image 
            ? `<img src="${place.image}" alt="${place.name}" class="place-image">`
            : `<div class="image-placeholder"><i class="fas fa-image"></i></div>`;
        
        const cardHTML = `
            <div class="card-wrapper" data-category="${place.category}" data-city="${place.city}">
                <div class="card">
                    <div class="card-image-container">
                        <div class="card-image">
                            ${imageContent}
                            <div class="image-overlay"></div>
                        </div>
                        <div class="card-badges">
                            <span class="category-badge">
                                <i class="fas fa-gopuram"></i> ${categoryDisplay}
                            </span>
                            <div class="rating-badge">
                                <i class="fas fa-star"></i> ${place.rating ? place.rating.toFixed(1) : '4.5'}
                            </div>
                        </div>
                        <button class="favorite-btn" onclick="toggleFavorite(this)">
                            <i class="far fa-heart"></i>
                        </button>
                    </div>
                    <div class="card-content">
                        <h3 class="card-title">${place.name}</h3>
                        <p class="card-description">${place.description.substring(0, 85)}...</p>
                        
                        <div class="card-meta">
                            <span class="meta-item">
                                <i class="fas fa-map-pin"></i> ${place.location}
                            </span>
                            <span class="meta-item">
                                <i class="fas fa-building"></i> ${cityDisplay}
                            </span>
                        </div>

                        <div class="card-tags">
                            <span class="tag">Popular</span>
                            <span class="tag">Local Favorite</span>
                        </div>
                    </div>
                    <div class="card-actions">
                        <button class="btn-action btn-primary" onclick="openModal(${JSON.stringify(place).replace(/"/g, '&quot;')})">
                            <i class="fas fa-eye"></i> View Details
                        </button>
                        <button class="btn-action btn-secondary">
                            <i class="fas fa-bookmark"></i> Save
                        </button>
                    </div>
                </div>
            </div>
        `;
        placesContainer.innerHTML += cardHTML;
    });
}

/* ========== FILTER BY CATEGORY ========== */
function filterCategory(category) {
    currentFilter = category;
    
    // Update active button
    filterBtns.forEach(btn => {
        btn.classList.remove('active');
        if (btn.getAttribute('data-filter') === category) {
            btn.classList.add('active');
        }
    });

    // Fetch places with new filter
    fetchPlacesFromAPI();
}

/* ========== TOGGLE FAVORITE ========== */
function toggleFavorite(btn) {
    btn.classList.toggle('active');
    
    if (btn.classList.contains('active')) {
        btn.innerHTML = '<i class="fas fa-heart"></i>';
    } else {
        btn.innerHTML = '<i class="far fa-heart"></i>';
    }
}

/* ========== THEME TOGGLE ========== */
function toggleTheme() {
    document.body.classList.toggle('dark-mode');
    
    if (document.body.classList.contains('dark-mode')) {
        themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        localStorage.setItem('theme', 'dark');
    } else {
        themeToggle.innerHTML = '<i class="fas fa-moon"></i>';
        localStorage.setItem('theme', 'light');
    }
}

/* ========== MODAL FUNCTIONS ========== */
function openModal(place) {
    const modal = document.getElementById('detailsModal');
    
    // Format category name
    const categoryDisplay = place.category === 'hidden_spots' ? 'Hidden Spots' : 
                           place.category === 'falls' ? 'Waterfalls' :
                           place.category.charAt(0).toUpperCase() + place.category.slice(1);
    
    // Format city name
    const cityDisplay = place.city.charAt(0).toUpperCase() + place.city.slice(1);
    
    // Update modal content
    document.getElementById('modalPlaceName').textContent = place.name;
    document.getElementById('modalCategory').textContent = categoryDisplay;
    document.getElementById('modalLocation').textContent = place.location;
    document.getElementById('modalCity').textContent = cityDisplay;
    document.getElementById('modalRating').textContent = (place.rating ? place.rating.toFixed(1) : '4.5') + ' / 5';
    document.getElementById('modalDescription').textContent = place.description;
    
    // Open modal
    modal.classList.add('active');
    document.body.style.overflow = 'hidden';
}

function closeModal() {
    const modal = document.getElementById('detailsModal');
    modal.classList.remove('active');
    document.body.style.overflow = 'auto';
}

// Close modal when clicking outside the content
window.addEventListener('click', (e) => {
    const modal = document.getElementById('detailsModal');
    if (e.target === modal) {
        closeModal();
    }
});

// Close modal with Escape key
window.addEventListener('keydown', (e) => {
    if (e.key === 'Escape') {
        closeModal();
    }
});

// Load theme preference
window.addEventListener('load', () => {
    const theme = localStorage.getItem('theme') || 'light';
    if (theme === 'dark') {
        document.body.classList.add('dark-mode');
        if (themeToggle) {
            themeToggle.innerHTML = '<i class="fas fa-sun"></i>';
        }
    }
});