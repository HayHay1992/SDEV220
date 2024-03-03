DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}



TIME_ZONE = 'America/Fort_Wayne'

LANGUAGE_CODE = 'en-us'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / 'static

ALLOWED_HOSTS = ['127.0.0.1', '.pythonanywhere.com']

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
]
