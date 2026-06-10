# Quick API Reference Guide

## Base URL
```
http://localhost:8000
```

---



### 1. **Search Places** (General)
```
GET /api/search/
```

**Query Parameters:**
- `q` (string) - Search query
- `category` (string) - Filter by category: `all`, `temple`, `hidden_spots`, `falls`, `food`

**Examples:**
```bash
# Search for "temple"
/api/search/?q=temple

# Get all waterfalls
/api/search/?category=falls

# Search for "monkey" in all categories
/api/search/?q=monkey&category=all
```

**Sample Response:**
```json
{
  "results": [
    {
      "id": 1,
      "name": "Monkey Falls",
      "description": "Cascading waterfall hidden deep...",
      "location": "Parambikulam Forest",
      "category": "falls",
      "city": "pollachi",
      "rating": 4.5,
      "image": null
    }
  ]
}
```

---

### 2. **Hidden Places API** (New)
```
GET /api/hidden-places/
```

**Query Parameters:**
- `category` (string) - `all`, `hidden_spots`, `falls`, `temple`, `food`
- `search` (string) - Search query
- `city` (string) - City name (default: `pollachi`)

**Examples:**
```bash
# Get all places in Pollachi (default)
/api/hidden-places/

# Get only hidden spots
/api/hidden-places/?category=hidden_spots

# Search for "river"
/api/hidden-places/?search=river

# Get temples with search
/api/hidden-places/?category=temple&search=temple

# Get food places in a different city
/api/hidden-places/?city=coimbatore&category=food
```

**Sample Response:**
```json
{
  "count": 6,
  "city": "pollachi",
  "places": [
    {
      "id": 26,
      "name": "Loam's Viewpoint",
      "description": "Stunning panoramic views of the Western Ghats...",
      "location": "Valparai Road",
      "category": "hidden_spots",
      "city": "pollachi",
      "rating": 4.5,
      "image": null
    },
    {
      "id": 27,
      "name": "Vazhiyar Valley",
      "description": "A serene valley tucked away from main roads...",
      "location": "Valparai Area",
      "category": "hidden_spots",
      "city": "pollachi",
      "rating": 4.5,
      "image": null
    }
  ],
  "categories": {
    "hidden_spots": 6,
    "falls": 4,
    "temple": 4,
    "food": 4
  }
}
```

---

## Code Examples

### JavaScript Fetch
```javascript
// Get all hidden spots
fetch('/api/hidden-places/?category=hidden_spots')
  .then(response => response.json())
  .then(data => {
    console.log(`Found ${data.count} locations`);
    data.places.forEach(place => {
      console.log(`${place.name} (${place.rating}⭐)`);
    });
  })
  .catch(error => console.error('Error:', error));
```

### JavaScript Async/Await
```javascript
async function getWaterfalls() {
  try {
    const response = await fetch('/api/hidden-places/?category=falls');
    const data = await response.json();
    
    console.log('Available waterfalls:');
    data.places.forEach(place => {
      console.log(`- ${place.name}`);
      console.log(`  Location: ${place.location}`);
      console.log(`  Rating: ${place.rating} / 5`);
    });
    
    return data.places;
  } catch (error) {
    console.error('Failed to fetch waterfalls:', error);
  }
}

getWaterfalls();
```

### Python Requests
```python
import requests

# Get all temples
response = requests.get('http://localhost:8000/api/hidden-places/', {
    'category': 'temple'
})

if response.status_code == 200:
    data = response.json()
    print(f"Found {data['count']} temples")
    
    for place in data['places']:
        print(f"\n{place['name']}")
        print(f"Location: {place['location']}")
        print(f"Description: {place['description'][:50]}...")
        print(f"Rating: {place['rating']}/5")
else:
    print(f"Error: {response.status_code}")
```

### cURL Examples
```bash
# Get all places
curl "http://localhost:8000/api/hidden-places/"

# Filter by category
curl "http://localhost:8000/api/hidden-places/?category=falls"

# Search for location
curl "http://localhost:8000/api/hidden-places/?search=valley"

# Pretty print JSON (requires jq)
curl "http://localhost:8000/api/hidden-places/" | jq '.'

# Count places by category
curl "http://localhost:8000/api/hidden-places/" | jq '.categories'
```

---

## Category Codes

| Code | Display | Count |
|------|---------|-------|
| `hidden_spots` | Hidden Spots | 6 |
| `falls` | Waterfalls | 4 |
| `temple` | Temple | 4 |
| `food` | Food | 4 |

---

## Location Breakdown

### Hidden Spots (6)
1. Loam's Viewpoint
2. Vazhiyar Valley
3. Uppar River Scenic Spot
4. Kaka Kothi Parai
5. Vettaikaranpudur Village Roads
6. Anikkadavu Rural Areas

### Waterfalls (4)
1. Monkey Falls
2. Panchalingam Falls
3. Siruvani Waterfalls
4. Aliyar Check Dam Small Waterfalls

### Temples (4)
1. Masani Amman Temple
2. Bhramaram Sivan Temple
3. Aliyar Arivu Thirukovil
4. Small Village Vinayagar Temples

### Food (4)
1. Pollachi Market Street Evening Food Zone
2. Mahalingapuram Night Food Streets
3. Fire Station Area Egg Appam Shops
4. Roadside Bajji & Bonda Shops

---

## Tips

✅ Use `/api/hidden-places/` for location-specific queries
✅ Use `/api/search/` for general searches across all fields
✅ Both endpoints support pagination (if added later)
✅ Ratings are dynamic and can be updated via Django admin
✅ Images can be added per location for rich presentation

---

## Troubleshooting

**Q: "404 Not Found" on API endpoint**
A: Ensure Django server is running and check the URL matches exactly

**Q: Empty results**
A: Check if you're filtering by correct category name
A: Make sure database has data: `python manage.py shell`

**Q: CORS errors in browser**
A: Add Django CORS headers if needed:
```bash
pip install django-cors-headers
```

---

Generated: March 2026
Version: 1.0
