"""
Django settings for text_reader project.

Generated by 'django-admin startproject' using Django 3.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.1/ref/settings/
"""
import os
import platform
import sys
from logging.handlers import SysLogHandler

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'i&ka%-sova@a^n!np_80t2vt%1$y($tmj^)bsb6ta_hmzbxpfs'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

CORS_ORIGIN_ALLOW_ALL = True
ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

THIRD_PARTY_APPS = [
    'bootstrap4',
    'rest_framework',
    'simple_history',
    'storages',
    'waffle',
]

PROJECT_APPS = [
    'text_reader.apps.core',
    'text_reader.apps.users',
    'text_reader.apps.textreader',
]

INSTALLED_APPS += THIRD_PARTY_APPS
INSTALLED_APPS += PROJECT_APPS

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'waffle.middleware.WaffleMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',
]

ROOT_URLCONF = 'text_reader.urls'

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
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.contrib.messages.context_processors.messages',

                'text_reader.apps.core.context_processors.site_processor',
            ],
        },
    },
]

WSGI_APPLICATION = 'text_reader.wsgi.application'

# ------------------------------
# AUTHORIZATION

# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-user-model
# https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#using-a-custom-user-model-when-starting-a-project
AUTH_USER_MODEL = 'users.User'

LOGIN_URL = '/login/'
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
# ------------------------------
# ------------------------------
# AUTHENTICATION CONFIGURATION
# https://docs.djangoproject.com/en/2.1/topics/auth/customizing/#customizing-authentication-in-django
# https://django-oauth-toolkit.readthedocs.io/en/latest/rest-framework/getting_started.html

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)
# ------------------------------
# ------------------------------
# CACHE CONFIGURATION
# See: https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
    }
}
# ------------------------------
# ------------------------------
# Database Configuration
# https://docs.djangoproject.com/en/3.1/ref/settings/#databases

# # DEVELOPMENT POSTGRESQL DATABASE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.postgresql_psycopg2',
#         'NAME': 'DB_NAME',
#         'USER': 'DB_USER',
#         'PASSWORD': 'DB_PASSWORD',
#         'HOST': 'localhost',    # Or an IP Address that your DB is hosted on
#         'PORT': '5432',
#     }
# }
#
# # PRODUCTION MYSQL DATABASE
# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.mysql',
#         'NAME': 'DB_NAME',
#         'USER': 'DB_USER',
#         'PASSWORD': 'DB_PASSWORD',
#         'HOST': 'localhost',    # Or an IP Address that your DB is hosted on
#         'PORT': '3306',
#     }
# }
#
# # HEROKU DATABASE CONFIGURATION
# import dj_database_url
# DATABASES = {
#     'default': dj_database_url.config()
# }
#
# # Honor the 'X-Forwarded-Proto' header for request.is_secure()
# SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')

# ------------------------------

# Password validation
# https://docs.djangoproject.com/en/3.1/ref/settings/#auth-password-validators

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

# See: https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# Internationalization
# https://docs.djangoproject.com/en/3.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'

# ------------------------------
# MEDIA CONFIGURATION

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.1/howto/static-files/

STATIC_URL = '/static/'
# STATIC_ROOT = os.path.join(BASE_DIR, "static/")
# STATIC_ROOT = 'staticfiles'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# Add media directory and its base url for user uploads
MEDIA_URL = '/site_media/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "site_media/")

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
    os.path.join(BASE_DIR, 'project_static'),
)

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

# Simplified static file serving.
# https://warehouse.python.org/project/whitenoise/

# STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
# ------------------------------
# ------------------------------
# LOGGING CONFIGURATION

# LOGGING = {
#     'version': 1,
#     'disable_existing_loggers': False,
#     'formatters': {
#         'verbose': {
#             'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
#             'datefmt': "%d/%b/%Y %H:%M:%S"
#         },
#         'simple': {
#             'format': '%(levelname)s %(message)s'
#         },
#     },
#     'filters': {
#         'require_debug_false': {
#             '()': 'django.utils.log.RequireDebugFalse'
#         }
#     },
#     'handlers': {
#         'mail_admins': {
#             'level': 'ERROR',
#             'filters': ['require_debug_false'],
#             'class': 'django.utils.log.AdminEmailHandler',
#             'formatter': 'verbose'
#         },
#         'console': {
#             'level': 'ERROR',
#             'class': 'logging.StreamHandler',
#             'stream': sys.stdout,
#             'formatter': 'verbose'
#         },
#         'file': {
#             'level': 'ERROR',
#             'class': 'logging.FileHandler',
#             'filename': 'logs/text_reader.log',
#             'formatter': 'verbose'
#         },
#     },
#     'loggers': {
#         'django': {
#             'handlers': ['console', 'file'],
#             'propagate': True,
#             'level': 'ERROR',
#         },
#         'django.request': {
#             'handlers': ['mail_admins'],
#             'level': 'ERROR',
#             'propagate': True,
#         },
#         '': {   # generic logger for all django apps. For specific app use format like 'cms.views'.
#             'handlers': ['console', 'file'],
#             'level': 'ERROR'
#         },
#     }
# }


# LOGGING CONFIGURATION
# Set up logging for development use (logging to stdout)
level = 'DEBUG' if DEBUG else 'INFO'
hostname = platform.node().split(".")[0]

# Use a different address for Mac OS X
syslog_address = '/var/run/syslog' if platform.system().lower() == 'darwin' else '/dev/log'
syslog_format = '[service_variant=text-reader][%(name)s] %(levelname)s [{hostname}  %(process)d] ' \
                '[%(pathname)s:%(lineno)d] - %(message)s'.format(hostname=hostname)

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'standard': {
            'format': '%(asctime)s %(levelname)s %(process)d [%(name)s] %(pathname)s:%(lineno)d - %(message)s',
        },
        'syslog_format': {'format': syslog_format},
    },
    'handlers': {
        'console': {
            'level': level,
            'class': 'logging.StreamHandler',
            'formatter': 'standard',
            'stream': 'ext://sys.stdout',
        },
        'local': {
            'level': level,
            'class': 'logging.handlers.SysLogHandler',
            'address': syslog_address,
            'formatter': 'syslog_format',
            'facility': SysLogHandler.LOG_LOCAL0,
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console', 'local'],
            'propagate': True,
            'level': 'INFO'
        },
        'requests': {
            'handlers': ['console', 'local'],
            'propagate': True,
            'level': 'WARNING'
        },
        'factory': {
            'handlers': ['console', 'local'],
            'propagate': True,
            'level': 'WARNING'
        },
        'elasticsearch': {
            'handlers': ['console', 'local'],
            'propagate': True,
            'level': 'WARNING'
        },
        'urllib3': {
            'handlers': ['console', 'local'],
            'propagate': True,
            'level': 'WARNING'
        },
        'django.request': {
            'handlers': ['console', 'local'],
            'propagate': True,
            'level': 'WARNING'
        },
        '': {
            'handlers': ['console', 'local'],
            'level': 'DEBUG',
            'propagate': False
        },
    }
}
# END LOGGING CONFIGURATION
# ------------------------------
