# -*- coding=utf-8 -*-
from settings import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

ADMIN_MEDIA_PREFIX = '/static/admin/'
STATIC_URL = '/static/'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql', # Add 'postgresql_psycopg2', 'postgresql', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': 'censuratore',                      # Or path to database file if using sqlite3.
        'USER': 'user',                      # Not used with sqlite3.
        'PASSWORD': 'user',                  # Not used with sqlite3.
        'HOST': '127.0.0.1',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '',                      # Set to empty string for default. Not used with sqlite3.
    }
}

CACHES = {
    'default': {
        'BACKEND': 'django.core.cache.backends.dummy.DummyCache',
    }
}

MEDIA_ROOT = os.path.join(PROJECT_ROOT, "..", "media/censuratore", *MEDIA_URL.strip("/").split("/"))
NUHP_STATIC_URL = "http://www.stqn.it/stage/nuhp_static"
NEWRELIC_INI_PATH = ''

LOGGING["handlers"]["console"] = {
    'level': 'DEBUG',
    'class': 'logging.StreamHandler'
}
LOGGING["loggers"]['pensieve'] = {
    'handlers': ['console'],
    'level': 'DEBUG',
    'propagate': True
}
# silent raven
RAVEN_CONFIG = {
    'dns': '',
}
