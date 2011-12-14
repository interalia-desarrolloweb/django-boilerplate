# -*- coding: utf-8 -*-

"""
    Bootstrap settings
    Authors  :   [ 
                    Alvaro Lizama Molina <alvaro.lizama@interalia.net>
                 ]
"""

import os
gettext = lambda s: s
PROJECT_PATH = os.path.abspath(os.path.dirname(__file__))


## DEBUG
#############################################################
DEBUG = False
TEMPLATE_DEBUG = False
LOCAL = False


## ADMINS
#############################################################
ADMINS = (
    ('Alvaro Lizama', 'alvaro.lizama@interalia.net'),
)

MANAGERS = ADMINS


## DATABASES
#############################################################
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '',                      # Or path to database file if using sqlite3.
        'USER': '',                      # Not used with sqlite3.
        'PASSWORD': '',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}


## TIME ZONE
#############################################################
TIME_ZONE = 'America/Mexico_City'
LANGUAGE_CODE = 'es-MX'
SITE_ID = 1
USE_I18N = True
USE_L10N = True


## MEDIA AND STATIC FILES
#############################################################
MEDIA_URL = '/media/'
MEDIA_ROOT = PROJECT_PATH + MEDIA_URL

STATIC_URL = '/static/'
STATIC_ROOT = PROJECT_PATH + STATIC_URL

ADMIN_MEDIA_PREFIX = STATIC_URL + 'admin/'

STATICFILES_DIRS = (
    MEDIA_ROOT,
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


## SECURITY
#############################################################
SECRET_KEY = 'pq3*y%&)!+vamm21mawl$i&5na3e^2p4)mrbjxdvlv)a=1-hv$'


## MIDDLEWARES
#############################################################
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)


## TEMPLATES
#############################################################
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_DIRS = (
    PROJECT_PATH + '/templates',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
)


## URLS
#############################################################
ROOT_URLCONF = 'urls'


## APPS
#############################################################
INSTALLED_APPS = (
    # Fluent dashboard
    'fluent_dashboard',
    # Admin tools
    'admin_tools',
    'admin_tools.theming',
    'admin_tools.menu',
    'admin_tools.dashboard',
    # Basic Django Apps 
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    # South
    'south',
    # Apps
    'main',
)


## ADMIN TOOLS
#############################################################
ADMIN_TOOLS_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentIndexDashboard'
ADMIN_TOOLS_APP_INDEX_DASHBOARD = 'fluent_dashboard.dashboard.FluentAppIndexDashboard'
ADMIN_TOOLS_MENU = 'fluent_dashboard.menu.FluentMenu'


## LOGS
#############################################################
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}


## LOCAL SETTINGS
#############################################################
try: 
    from local_settings import *
except:
    pass
