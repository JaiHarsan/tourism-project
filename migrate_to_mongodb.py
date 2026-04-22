"""
Script to migrate places data from SQLite to MongoDB
"""
import os
import sys
import json
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tourism_platform.settings')
django.setup()

from places.models import Place as MongoPlace

# Load data from SQLite backup JSON
def migrate_data():
    try:
        with open('places_backup.json', 'r') as f:
            data = json.load(f)
        
        print(f"Found {len(data)} records to migrate...")
        
        migrated = 0
        skipped = 0
        
        for item in data:
            try:
                place_data = item['fields']
                place_data['name'] = place_data.get('name', '')
                place_data['description'] = place_data.get('description', '')
                place_data['location'] = place_data.get('location', '')
                place_data['category'] = place_data.get('category', 'temple')
                place_data['city'] = place_data.get('city', 'coimbatore')
                place_data['image'] = place_data.get('image', None)
                place_data['rating'] = place_data.get('rating', 4.5)
                
                # Check if place already exists
                existing = MongoPlace.objects.filter(
                    name__exact=place_data['name'],
                    city__exact=place_data['city']
                )
                
                if existing:
                    print(f"✓ Skipped (exists): {place_data['name']}")
                    skipped += 1
                else:
                    place = MongoPlace(**place_data)
                    place.save()
                    print(f"✓ Migrated: {place_data['name']} ({place_data['city']})")
                    migrated += 1
                    
            except Exception as e:
                print(f"✗ Error migrating place: {e}")
                skipped += 1
        
        print(f"\n{'='*60}")
        print(f"Migration Complete!")
        print(f"Migrated: {migrated}, Skipped: {skipped}")
        print(f"Total places in MongoDB: {MongoPlace.objects.count()}")
        print(f"{'='*60}")
        
    except FileNotFoundError:
        print("❌ places_backup.json not found. Run backup first.")
    except Exception as e:
        print(f"❌ Migration error: {e}")

if __name__ == '__main__':
    migrate_data()
