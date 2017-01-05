"""
Django settings for web project.

Generated by 'django-admin startproject' using Django 1.10.3.

For more information on this file, see
https://docs.djangoproject.com/en/1.10/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.10/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.10/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'u@kd9ll!e=l&w&qs3=5$ih9=c&3k-#%in_)r5bk$@npza7xp%_'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

SITETREE_RAISE_ITEMS_ERRORS_ON_DEBUG = True

ALLOWED_HOSTS = ['.da02.delphin-amazonia.ch',
                 '.da02.delphin-amazonia.ch.',
                 'localhost',]


# Application definition

INSTALLED_APPS = [
    'security',
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bootstrap3',
    'django_tables2',
    'django_xworkflows',
    'sitetree',
    'dashing',
    'ckeditor',
    'polymorphic_tree',
    'polymorphic',
    'mptt',
    'django_mptt_admin',
    #'genericadmin',
    'treebeard',
    'web',
    #'filer',
    #'easy_thumbnails',
    #'calendarium',
    'crispy_forms',
    'generic_scaffold',
    'actions',
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

ROOT_URLCONF = 'webapp.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
            'loaders': [
                ('django.template.loaders.cached.Loader',[
                    'django.template.loaders.filesystem.Loader',
                    'django.template.loaders.app_directories.Loader',
                    'admin_tools.template_loaders.Loader',
                    ]
                 ),
            ],
        },
    },
]

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.db.DatabaseCache',
        'LOCATION': 'my_cache_table',
    }
}

WSGI_APPLICATION = 'webapp.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
    'ENGINE':   'django.db.backends.oracle',
    'NAME':     'daoda1scan/SHCDBT4_PRI.da02.delphin-amazonia.ch',
    #'NAME':     'ORCL',
    #'HOST':     'localhost',
    #'PORT':     '1521',
    'USER':     'DAPY',
    'PASSWORD': 'zebex'
  }
}

# CKEditor Settings
# https://github.com/django-ckeditor/django-ckeditor/#installation

CKEDITOR_JQUERY_URL = '//ajax.googleapis.com/ajax/libs/jquery/2.1.1/jquery.min.js'

# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'de-ch'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.10/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]

# Sende emails durch folgende Einstellungen
EMAIL_HOST = 'mail.intranet.ch'
EMAIL_PORT = 25
EMAIL_USE_SSL = False

# =====================================

from django_auth_ldap.config import LDAPSearch, NestedActiveDirectoryGroupType
import ldap


# Binding and connection options
AUTH_LDAP_SERVER_URI = "ldap://ldap.intranet.ch:389"
AUTH_LDAP_BIND_DN = "CN=ldap-query,OU=Service,OU=Konten,OU=Delphin,DC=da02,DC=delphin-amazonia,DC=ch"
AUTH_LDAP_BIND_PASSWORD = "queryntdmn"
AUTH_LDAP_CONNECTION_OPTIONS = {
    ldap.OPT_DEBUG_LEVEL: 2,
    ldap.OPT_REFERRALS: 0,
}
# What to do once the user is authenticated
AUTH_LDAP_USER_ATTR_MAP = {
    "first_name": "givenName",
    "last_name": "sn",
    "email": "mail"
}
# User and group search objects and types
AUTH_LDAP_USER_SEARCH = LDAPSearch("OU=DA_7,OU=Benutzer,OU=Konten,OU=Delphin,DC=da02,DC=delphin-amazonia,DC=ch",
    ldap.SCOPE_SUBTREE, "(sAMAccountName=%(user)s)")
AUTH_LDAP_GROUP_SEARCH = LDAPSearch("OU=DA-Sicherheit,OU=Gruppen,OU=Delphin,DC=da02,DC=delphin-amazonia,DC=ch",
    ldap.SCOPE_SUBTREE, "(objectClass=group)")
AUTH_LDAP_GROUP_TYPE = NestedActiveDirectoryGroupType()

# Cache settings
AUTH_LDAP_CACHE_GROUPS = True
AUTH_LDAP_GROUP_CACHE_TIMEOUT = 300


AUTH_LDAP_USER_FLAGS_BY_GROUP = {
    "is_admin": ["CN=_DA_AGR-APEX-ADMIN,OU=DA-Sicherheit,OU=Gruppen,OU=Delphin,DC=da02,DC=delphin-amazonia,DC=ch"],
    "is_buchhaltung": ["CN=_DA_AGR-APEX-BUCHHALTUNG,OU=DA-Sicherheit,OU=Gruppen,OU=Delphin,DC=da02,DC=delphin-amazonia,DC=ch"],
    "is_superuser": ["CN=_DA_AGR-APEX-SUPERUSER,OU=DA-Sicherheit,OU=Gruppen,OU=Delphin,DC=da02,DC=delphin-amazonia,DC=ch"],
    "is_user": ["CN=_DA_AGR-APEX-USER,OU=DA-Sicherheit,OU=Gruppen,OU=Delphin,DC=da02,DC=delphin-amazonia,DC=ch"],
    "is_staff": ["CN=_DA_AGR-APEX-USER,OU=DA-Sicherheit,OU=Gruppen,OU=Delphin,DC=da02,DC=delphin-amazonia,DC=ch"],
}
AUTH_LDAP_FIND_GROUP_PERMS = True

# =============================================

AUTHENTICATION_BACKENDS = (

    'django_auth_ldap.backend.LDAPBackend',
    'django.contrib.auth.backends.ModelBackend',
 #   'account.authentication.EmailAuthBackend',

)

REDIS_HOST = 'localhost'
REDIS_PORT = 6379
REDIS_DB = 0

LOGIN_REDIRECT_URL = "/"
