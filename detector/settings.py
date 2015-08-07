# -*- coding: utf-8 -*-
"""
Django settings for detector project.

Generated by 'django-admin startproject' using Django 1.8.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c+s+l+zqffw42%rhl23#h(_h1e!-p!=&7yiwdz_om9#ip5o2h)'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'lightsite',
    'django_summernote',
    'widget_tweaks',
    'registration',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'detector.urls'

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
                "django.core.context_processors.media",
                "django.core.context_processors.static",
            ],
        },
    },
]

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    #     'django.template.loaders.eggs.Loader',
)

WSGI_APPLICATION = 'detector.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {}

# Parse database configuration from $DATABASE_URL
import dj_database_url

DEFAULT_DATABASE_URL = os.environ.get('DATABASE_URL','postgres://postgres:1@localhost:5432/deta')
DATABASES['default'] = dj_database_url.config(default=DEFAULT_DATABASE_URL)
DATABASES['default']['ENGINE'] = 'django_postgrespool'

# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/
APP_NAME = 'detector'
STATIC_ROOT = 'staticfiles'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

SERIAL_DIRNAME = 'serial'
LOGO_DIRNAME = 'logos'
PHOTO_DIRNAME = 'photos'

# http://www.effectivedjango.com/tutorial/authzn.html
# LOGIN_REDIRECT_URL = '/'
# LOGIN_URL = 'django.contrib.auth.views.login'

SUMMERNOTE_CONFIG = {  # Or, set editor language/locale forcely
                       'lang': 'ru-RU',

                       'width': '100%',
                       'height': '480',

                       'toolbar': [
                           ['style', ['style', 'bold', 'italic', 'underline', 'clear', 'fontsize']],
                           ['para', ['ul', 'ol', 'paragraph']],
                           ['insert', ['link', 'table', 'hr', 'picture']],
                           ['misc', ['undo', 'redo']],

                       ],

                       }

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')

# http://www.tangowithdjango.com/book17/chapters/login_redux.html
REGISTRATION_OPEN = True                # If True, users can register
ACCOUNT_ACTIVATION_DAYS = 7     # One-week activation window; you may, of course, use a different value.
REGISTRATION_AUTO_LOGIN = True  # If True, the user will be automatically logged in.
LOGIN_REDIRECT_URL = '/companies'  # The page you want users to arrive at after they successful log in
LOGIN_URL = '/login/'  # The page users are directed to if they are not logged in and are trying to access pages requiring authentication

print ('STATIC_ROOT', STATIC_ROOT)
print ('STATICFILES_DIRS', STATICFILES_DIRS)
print ('MEDIA_ROOT', MEDIA_ROOT)
print ('DEFAULT_DATABASE_URL', DEFAULT_DATABASE_URL)
print ('EMAIL_HOST_USER', EMAIL_HOST_USER)
print ('EMAIL_HOST_PASSWORD', EMAIL_HOST_PASSWORD)
