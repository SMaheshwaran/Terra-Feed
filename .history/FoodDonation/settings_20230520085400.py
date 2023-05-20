import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = '9u1n4mtpr_0+onmagrye0jl68dqc^g!br_d2x&=w*ln3_fl=g'

DEBUG = True

ALLOWED_HOSTS = []  # Add your domain names or IPs here when DEBUG is False

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'food',  # Add your app name here
]

# Other settings...

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

# Other settings...

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Other settings...

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

# Other settings...

LOGIN_REDIRECT_URL = 'afterlogin'  # Update with your desired redirect URL
LOGOUT_REDIRECT_URL = 'home'  # Update with your desired redirect URL

# Other settings...
