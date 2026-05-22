/* ========== DOM ELEMENTS ========== */
const searchInput = document.getElementById('searchInput');
const placesContainer = document.getElementById('placesContainer');
const emptyState = document.getElementById('emptyState');
const themeToggle = document.getElementById('themeToggle');
const priceRange = document.getElementById('priceRange');
const sortBy = document.getElementById('sortBy');


let allCards = [];
let currentFilter = 'all';
let currentSort = 'newest';


document.addEventListener('DOMContentLoaded', () => {
    allCards = document.querySelectorAll('.card-wrapper');
    
   
    filterBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            const filter = btn.getAttribute('data-filter');
            filterCategory(filter);
        });
    });

    // Search functionality
    if (searchInput) {
        searchInput.addEventListener('keyup', performSearch);
    }

    // Price range
    if (priceRange) {
        priceRange.addEventListener('input', performFilter);
    }

    // Sort
    if (sortBy) {
        sortBy.addEventListener('change', (e) => {
            currentSort = e.target.value;
            performFilter();
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
});

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

    performFilter();
}

/* ========== PERFORM FILTER ========== */
function performFilter() {
    let visibleCount = 0;

    allCards.forEach(cardWrapper => {
        const card = cardWrapper.querySelector('.card');
        const cardCategory = cardWrapper.getAttribute('data-category') || 'all';
        const title = card.querySelector('.card-title').textContent.toLowerCase();
        const description = card.querySelector('.card-description').textContent.toLowerCase();
        const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';

        // Check filters
        const categoryMatch = currentFilter === 'all' || cardCategory === currentFilter;
        const searchMatch = title.includes(searchTerm) || description.includes(searchTerm);

        if (categoryMatch && searchMatch) {
            cardWrapper.style.display = 'block';
            visibleCount++;
        } else {
            cardWrapper.style.display = 'none';
        }
    });

    // Show/hide empty state
    if (emptyState) {
        emptyState.style.display = visibleCount === 0 ? 'block' : 'none';
    }
}

/* ========== SEARCH FUNCTIONALITY ========== */
function performSearch(e) {
    performFilter();
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
