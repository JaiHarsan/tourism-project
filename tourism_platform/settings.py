from pathlib import Path



SECRET_KEY = 'django-insecure-secret-key'

DEBUG = True

ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'places',
    'rest_framework',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'tourism_platform.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'places/templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'places.context_processors.user_context',  # Custom MongoDB user context
            ],
        },
    },
]

WSGI_APPLICATION = 'tourism_platform.wsgi.application'

# ✅ MongoDB Configuration
import mongoengine

# MongoDB Connection
MONGODB_DATABASES = {
    'default': {
        'name': 'tourism_db',
        'host': 'localhost',
        'port': 27017,
        # For MongoDB Atlas, use: 'host': 'mongodb+srv://username:password@cluster.mongodb.net/tourism_db?retryWrites=true&w=majority'
    }
}

# Connect to MongoDB
mongoengine.connect(
    db=MONGODB_DATABASES['default']['name'],
    host=MONGODB_DATABASES['default']['host'],
    port=MONGODB_DATABASES['default']['port'],
    connect=False,
    retryWrites=False
)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

AUTH_PASSWORD_VALIDATORS = []

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'Asia/Kolkata'
USE_I18N = True
USE_TZ = True

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'places/static']

MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ✅ Session Configuration for Proper Logout
SESSION_ENGINE = 'django.contrib.sessions.backends.db'  # Save sessions to database
SESSION_COOKIE_AGE = 1209600  # 2 weeks in seconds
SESSION_COOKIE_HTTPONLY = True  # Prevent JavaScript from accessing session
SESSION_COOKIE_SECURE = False  # Set to True in production with HTTPS
SESSION_COOKIE_SAMESITE = 'Lax'  # CSRF protection
SESSION_EXPIRE_AT_BROWSER_CLOSE = True  # Session expires when browser closes

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "places/static",
]
