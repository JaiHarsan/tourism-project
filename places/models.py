
from mongoengine import Document, StringField, FloatField, ImageField, ObjectIdField, BooleanField, EmailField
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash

class User(Document):
    """MongoDB User model for authentication"""
    username = StringField(max_length=100, required=True, unique=True)
    email = EmailField(required=True, unique=True)
    password = StringField(required=True)  # hashed password
    first_name = StringField(max_length=100, default='')
    last_name = StringField(max_length=100, default='')
    is_active = BooleanField(default=True)
    created_at = StringField(default=lambda: datetime.now().isoformat())
    updated_at = StringField(default=lambda: datetime.now().isoformat())
    
    meta = {
        'collection': 'users',
        'indexes': ['username', 'email']
    }
    
    def set_password(self, password):
        """Hash and set password"""
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        """Verify password"""
        return check_password_hash(self.password, password)
    
    def __str__(self):
        return self.username
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': str(self.id),
            'username': self.username,
            'email': self.email,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'created_at': self.created_at,
        }

class Place(Document):
    """MongoDB model for tourism places"""
    
    CATEGORY_CHOICES = [
        ('temple', 'Temple'),
        ('hidden_spots', 'Hidden Spots'),
        ('falls', 'Waterfalls'),
        ('food', 'Food'),
    ]
    
    CITY_CHOICES = [
        ('pollachi', 'Pollachi'),
        ('coimbatore', 'Coimbatore'),
        ('trichy', 'Trichy'),
        ('chennai', 'Chennai'),
        ('madurai', 'Madurai'),
    ]
    
    # Fields
    name = StringField(max_length=100, required=True)
    description = StringField(required=True)
    location = StringField(max_length=100, required=True)
    category = StringField(max_length=20, choices=CATEGORY_CHOICES, default='temple')
    city = StringField(max_length=20, choices=CITY_CHOICES, default='coimbatore')
    image = StringField(null=True, blank=True)  
    rating = FloatField(default=4.5)  
    created_at = StringField(default=lambda: datetime.now().isoformat())
    
    meta = {
        'collection': 'places',
        'indexes': ['city', 'category', 'name']
    }

    def __str__(self):
        return self.name
    
    def to_dict(self):
        """Convert to dictionary for API responses"""
        return {
            'id': str(self.id),
            'name': self.name,
            'description': self.description,
            'location': self.location,
            'category': self.category,
            'city': self.city,
            'image': self.image,
            'rating': self.rating,
        }