"""
Django settings for project2 project.

Generated by 'django-admin startproject' using Django 4.2.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import os.path
from pathlib import Path
from os import getenv

import environ


env=environ.Env(DEBUG=(bool,True))
environ.Env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG=env('DEBUG')

# SECURITY WARNING: keep the secret key used in production secret!

SECRET_KEY=env('SECRET_KEY')


ALLOWED_HOSTS = env('ALLOWED_HOSTS',cast=list) #.envde biz allowed hostda yalniz dirnaglarla ayirmisig ama normalda pythonun oxumasi ucun [] array seklinde olmalidir
                                              # ona gorede cast=list verdikki list kimi oxusun.

CSRF_TRUSTED_ORIGINS = env('CSRF_TRUSTED_ORIGINS',cast=list) #sitenin guvenli olmasi ucundur.


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'home',
    'product',
    'ckeditor',
    'ckeditor_uploader',
    'mptt',
    'user',
    'order',
    'storages',

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

ROOT_URLCONF = 'project2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'project2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': env.db()
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'az'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATICFILES_DIRS = [
    BASE_DIR / "static"
]

if DEBUG:
    STATIC_URL = '/static/'
    STATIC_ROOT = BASE_DIR / "staticfiles"
    MEDIA_URL = '/uploads/'
    MEDIA_ROOT = os.path.join(BASE_DIR, 'project2/uploads/')

    DEFAULT_FILE_STORAGE='django.core.files.storage.FileSystemStorage'

else:
    AWS_ACCESS_KEY_ID=env('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY=env('AWS_SECRET_ACCESS_KEY')
    AWS_STORAGE_BUCKET_NAME=env('AWS_STORAGE_BUCKET_NAME')
    AWS_S3_REGION_NAME=env('AWS_S3_REGION_NAME')


    DEFAULT_FILE_STORAGE = 'project2.custom_storages.MediaStorage'
    STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'

    AWS_DEFAULT_ACL= 'public-read'
    AWS_S3_BUCKET_PARAMETERS= {
        'Expires' : 'Thu, 31 Dec 2099 20:00:00 GMT',
        'CacheControl' : 'max-age=94608000',
    }

    STATIC_URL= f'https://{AWS_STORAGE_BUCKET_NAME}.s3.amazonaws.com/static/'
    STATIC_ROOT= STATIC_URL

    MEDIA_LOCATION= 'media'
    IMAGE_SETTING_LOCATION= MEDIA_LOCATION + '/image-settings'
    DOCUMENT_LOCATION= MEDIA_LOCATION + '/documents'



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'



CKEDITOR_JQUERY_URL='https://ajax.googleapis.com/ajax/libs/jquery/2.2.4/jquery.min.js'
CKEDITOR_UPLOAD_PATH='uploads/'
CKEDITOR_IMAGE_BACKEND="pillow"
CKEDITOR_CONFIGS= {
    'default' : {
        'toolbar' : None,
    }
}

