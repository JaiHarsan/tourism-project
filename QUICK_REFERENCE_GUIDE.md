# Tourism Platform - Quick Setup & Reference Guide

## 🚀 Quick Start

### Run the Application
```bash
# Activate virtual environment
venv\Scripts\Activate

# Start development server
python manage.py runserver

# Access application
# Frontend: http://localhost:8000/
# Admin: http://localhost:8000/admin/
```

### Populate Database with Default Data
```bash
python add_sample_data.py
```

---

## 📍 Available Cities & Places

### Pollachi (18 Places)
- Hidden Spots: 6
- Waterfalls: 4
- Temples: 4
- Food: 4

### Coimbatore (17 Places)
- Hidden Spots: 5
- Waterfalls: 4
- Temples: 4
- Food: 4

**Total: 35 places**

---

## 🎯 API Endpoints

### General Search (Searches Across All Fields & Cities)
```
GET /api/search/
Query: ?category=<cat>&q=<search>

Example: /api/search/?category=temple&q=ganesha
```

### Pollachi Places (City-Specific)
```
GET /api/hidden-places/
Query: ?category=<cat>&search=<query>

Examples:
- /api/hidden-places/
- /api/hidden-places/?category=hidden_spots
- /api/hidden-places/?search=valley
```

### Coimbatore Places (City-Specific)
```
GET /api/coimbatore-places/
Query: ?category=<cat>&search=<query>

Examples:
- /api/coimbatore-places/
- /api/coimbatore-places/?category=falls
- /api/coimbatore-places/?search=temple
```

### Category Codes
- `all` - All places
- `hidden_spots` - Hidden Spots / Scenic Spots
- `falls` - Waterfalls
- `temple` - Temples
- `food` - Street Food

---

## 📄 Key Files

### Backend
- `places/models.py` - Place model with rating field
- `places/views.py` - API endpoints (search, hidden_places, coimbatore_places)
- `places/urls.py` - Route definitions
- `places/serializers.py` - Serialization logic
- `add_sample_data.py` - Data population script

### Frontend
- `places/templates/base.html` - Main page with city tabs
- `places/static/js/script.js` - City switching, filtering, search logic
- `places/static/css/style.css` - Styling for city selector and cards

### Configuration
- `tourism_platform/settings.py` - Django settings
- `tourism_platform/urls.py` - Main URL router
- `places/migrations/` - Database migrations

---

## 🔧 Adding New Places

### Method 1: Edit Data Script
1. Open `add_sample_data.py`
2. Add to `places_data` list:
```python
{
    'name': 'Place Name',
    'description': 'Short 2-3 line description',
    'location': 'Location/Area Name',
    'category': 'hidden_spots|falls|temple|food',
    'city': 'coimbatore|pollachi',  # Add your city code
    'rating': 4.5
}
```
3. Run: `python add_sample_data.py`

### Method 2: Django Admin
1. Navigate to http://localhost:8000/admin/
2. Login with admin credentials
3. Click "Places" → "Add Place"
4. Fill in all fields:
   - Name: Required
   - Description: Required
   - Location: Required
   - Category: Choose from dropdown
   - City: Choose from dropdown (or add in models.py)
   - Rating: Decimal value (0-5)
   - Image: Optional file upload
5. Click "Save"

### Method 3: Django Shell
```bash
python manage.py shell
>>> from places.models import Place
>>> Place.objects.create(
...     name="New Place",
...     description="Description here",
...     location="Location",
...     category="hidden_spots",
...     city="coimbatore",
...     rating=4.7
... )
>>> exit()
```

---

## 🎨 Customization

### Add New City
1. Update `places/models.py`:
```python
CITY_CHOICES = [
    ('pollachi', 'Pollachi'),
    ('coimbatore', 'Coimbatore'),
    ('trichy', 'Trichy'),  # NEW
]
```

2. Create new API endpoint in `places/views.py`
3. Add route in `places/urls.py`
4. Add city tab in `places/templates/base.html`
5. Update `places/static/js/script.js` with city switching logic

### Change Colors
Edit `places/static/css/style.css`:
```css
:root {
    --primary-color: #7c3aed;      /* Purple */
    --secondary-color: #ec4899;    /* Pink */
    --accent-color: #f59e0b;       /* Amber */
}
```

### Add New Category
1. Update model in `places/models.py`:
```python
CATEGORY_CHOICES = [
    ('temple', 'Temple'),
    ('hidden_spots', 'Hidden Spots'),
    ('falls', 'Waterfalls'),
    ('food', 'Food'),
    ('beach', 'Beach'),  # NEW
]
```

2. Create migration: `python manage.py makemigrations`
3. Apply migration: `python manage.py migrate`
4. Add filter button in `places/templates/base.html`
5. Add places with new category to database

---

## 🧪 Testing

### Test All Endpoints
```bash
# Get all Pollachi places
curl "http://localhost:8000/api/hidden-places/"

# Get Coimbatore food places
curl "http://localhost:8000/api/coimbatore-places/?category=food"

# Search for temples
curl "http://localhost:8000/api/search/?category=temple&q=temple"

# With jq (pretty print)
curl "http://localhost:8000/api/coimbatore-places/" | jq '.'
```

### Database Queries
```bash
python manage.py shell
>>> from places.models import Place
>>> Place.objects.count()  # Total places
35
>>> Place.objects.filter(city='coimbatore').count()  # Coimbatore only
17
>>> Place.objects.filter(category='falls').values_list('name', flat=True)
# List all waterfalls
```

---

## 🐛 Common Issues & Solutions

| Issue | Cause | Solution |
|-------|-------|----------|
| "No module named places" | App not installed | Add 'places' to INSTALLED_APPS in settings.py |
| API returns empty | No data in DB | Run `python add_sample_data.py` |
| 404 on API endpoint | URL not registered | Check urls.py has correct paths |
| City tab doesn't work | JavaScript error | Check browser console, clear cache |
| Images not showing | No image uploaded | Use placeholder or upload image in admin |
| Database locked | Migration issue | Delete migrations (except __init__), reapply |

---

## 📦 Dependencies

### Core
- Django 6.0.3+
- djangorestframework
- Pillow (for images)

### Frontend
- Bootstrap (via CDN)
- Font Awesome (via CDN)
- Font: Poppins (Google Fonts)

### Development
- Python 3.9+
- pip / conda

---

## 🚀 Deployment Preparation

### Before Going Live

1. **Collect Real Images**
   - Upload via Django admin
   - Images go to `media/places/`

2. **Set Production Settings**
```python
# settings.py
DEBUG = False
ALLOWED_HOSTS = ['yourdomain.com']
SECRET_KEY = 'generateNewSecretKey'
```

3. **Create Superuser**
```bash
python manage.py createsuperuser
```

4. **Collect Static Files**
```bash
python manage.py collectstatic --noinput
```

5. **Backup Database**
```bash
python manage.py dumpdata > backup.json
```

6. **Use Production Server**
```bash
# NOT for production (use gunicorn, uWSGI, etc.)
# python manage.py runserver
gunicorn tourism_platform.wsgi:application --bind 0.0.0.0:8000
```

---

## 📊 Database Schema

### Place Model
```
id (AutoField) - Primary Key
name (CharField, 100) - Place name
description (TextField) - Detailed description
location (CharField, 100) - Location/area name
category (CharField, 20) - Category code
city (CharField, 20) - City code
image (ImageField) - Optional image file
rating (FloatField, default=4.5) - Rating 0-5
created_at (DateTimeField, auto_now_add=True) - Creation date
updated_at (DateTimeField, auto_now=True) - Last update date
```

---

## 🔐 Admin Credentials

Default (change after setup):
- URL: http://localhost:8000/admin/
- Username: admin
- Password: password

Create new admin:
```bash
python manage.py createsuperuser
```

---

## 📚 Documentation Files

1. **POLLACHI_HIDDEN_PLACES_UPDATE.md** - Initial Pollachi implementation
2. **API_QUICK_REFERENCE.md** - API usage guide with code examples
3. **COIMBATORE_INTEGRATION_GUIDE.md** - Coimbatore expansion guide
4. **This file** - General reference and quick start

---

## 💡 Tips & Tricks

### Performance
- Use pagination for APIs handling 100+ records
- Cache category listings for faster filtering
- Lazy load images on cards

### SEO
- Add meta tags per place
- Create sitemap.xml
- Add structured data (schema.org)

### User Experience
- Add favorite/bookmark functionality
- Create trip planning feature
- Add user ratings and reviews
- Implement sharing (social media)

### Future Features
- Google Maps integration
- Distance/directions API
- Weather integration
- Real-time availability
- Booking system
- Mobile app

---

## 📞 Support & Maintenance

### Regular Checks
- [ ] Monitor API response times
- [ ] Check error logs weekly
- [ ] Update images monthly
- [ ] Add new places quarterly
- [ ] Review user feedback

### Backup Strategy
```bash
# Weekly database backup
python manage.py dumpdata > backups/backup_$(date +%Y%m%d).json

# Restore from backup
python manage.py loaddata backups/backup_20260322.json
```

### Update Content
The `add_sample_data.py` script is safe to run multiple times - it auto-detects duplicates and skips them. You can:
1. Add new places to the script
2. Run `python add_sample_data.py`
3. Only new places will be created

---

**Last Updated:** March 2026  
**Version:** 2.0  
**Cities:** 2 (Pollachi, Coimbatore)  
**Total Places:** 35  
**Status:** ✅ Production Ready
