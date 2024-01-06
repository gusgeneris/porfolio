"""
Django settings for config project.
Generated by 'django-admin startproject' using Django 4.0.2.
"""

from pathlib import Path
from decouple import config

import os

import dj_database_url
#from dotenv import  load_dotenv, find_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'railway',
        'USER': 'root',
        'PASSWORD': '51hfAgB416EcfH2BdF2GHbgb-f2Cbhbh',
        'HOST': 'monorail.proxy.rlwy.net',
        'PORT': 57839,
    }
}



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',  
    # 'collectfast',  
    'django.contrib.staticfiles',
    'porfolioApp',
    'blogApp',

    'storages',
    'django_extensions',
    'ckeditor',
]
DEBUG = True

SECRET_KEY = 'django-insecure-+e!7*%ax%xu818^^i7@7hf-w9_st)%*v_he35nfm=e91#l*1ef'
STATIC_URL = 'static/'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'portfolioDjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'portfolioDjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

#load_dotenv(find_dotenv())

#DATABASES = {'default': dj_database_url.config(default='sqlite3:///db.sqlite', conn_max_age=600)}


# DATABASES = {
#     'default': {
#         'ENGINE':'django.db.backends.mysql',
#         'NAME':'railway',
#         'USER':'root',
#         'PASSWORD':'51hfAgB416EcfH2BdF2GHbgb-f2Cbhbh',
#         'HOST':'hmonorail.proxy.rlwy.net',
#         'PORT':57839,
#     }
# }
# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'es-ln'

TIME_ZONE = 'America/Buenos_Aires'

USE_I18N = True

USE_TZ = True


# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CKEDITOR_CONFIGS = {
    'default': {
        'toolbar': 'full',
    },
}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS= True
EMAIL_PORT = '587'
# EMAIL_HOST_USER = config('EMAIL_HOST_NAME')
# EMAIL_HOST_PASSWORD = config('EMAIL_HOST_PASSWORD')
