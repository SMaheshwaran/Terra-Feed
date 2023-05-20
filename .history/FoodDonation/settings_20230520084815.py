import os
from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')
STATIC_DIR = os.path.join(BASE_DIR, 'static')

# ... Rest of your settings ...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# ... Rest of your settings ...

STATICFILES_DIRS = [
    STATIC_DIR,
]

# ... Rest of your settings ...

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587
EMAIL_HOST_USER = 'justfortestingweb1@gmail.com'
EMAIL_HOST_PASSWORD = 'Maruti800'
EMAIL_RECEIVING_USER = ['justfortestingweb1@gmail.com']

# ... Rest of your settings ...