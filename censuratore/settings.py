# -*- coding=utf-8 -*-
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DEBUG = False
TEMPLATE_DEBUG = DEBUG

SECRET_KEY = '+ja$r7_pp_#4*jzmr0zbdum^$q$dfnsox&#y81bup^3#e_)1k#'

ALLOWED_HOSTS = ['.quotidiano.net', '.ilrestodelcarlino.it', '.lanazione.it', '.ilgiorno.it', '.cavallomagazine.it']

PROJECT_ROOT = BASE_DIR
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
STATIC_URL = '/static/'
STATIC_ROOT = 'static'
MEDIA_URL = '/media/'
MEDIA_ROOT = ''
STATICFILES_DIRS = (
)
ADMIN_MEDIA_PREFIX = STATIC_URL + "admin/"
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),
                 #os.path.join(PROJECT_ROOT, "pensieve/", "templates"),
                 )
ADMINS = (
    ('MonrifNet Dev', 'bugs@monrif.local'),
)
MANAGERS = ADMINS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = '192.168.21.25'
EMAIL_PORT = 25
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
)

NEWRELIC_INI_PATH = '/home/uwsgi/censuratore/censuratore/newrelic.ini'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'djcelery',
    'pensieve',
)

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
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

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.request",
    "censuratore.context_processors.basepaths",
    "censuratore.context_processors.extra_static_paths",
)

ROOT_URLCONF = 'censuratore.urls'

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

WSGI_APPLICATION = 'censuratore.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

LANGUAGE_CODE = 'it-IT'
TIME_ZONE = 'Europe/Rome'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

DATE_FORMAT = "d/m/Y"
TIME_FORMAT = "H:i"
DATETIME_FORMAT = "d/m/Y H:i"

MESSAGE_STORAGE = 'django.contrib.messages.storage.session.SessionStorage'

#
# Celery
#

CELERY_RESULT_BACKEND = 'cache+memcached://127.0.0.1:11211/'
CELERY_MESSAGE_COMPRESSION = 'gzip'
BROKER_URL = 'amqp://guest:guest@localhost:5672//'
CELERY_APP_NAME = 'censuratore'
# Sarebbe meglio usare json come formato di serializzazione,
# ma dà problemi con le date.
# CELERY_TASK_SERIALIZER = 'json'
CELERY_DEFAULT_QUEUE = 'censuratore'
from kombu import Exchange, Queue
CELERY_QUEUES = (
    Queue('censuratore', Exchange('default'), routing_key='censuratore'),
)

# Sentry
RAVEN_CONFIG = {
    'dsn': 'http://1346feebcb794766bd816ccffe8fcfd5:4a7622185dc644eb8b31b1b5cadd3688@192.168.21.144:9000/27',
}
try:
    import raven
    INSTALLED_APPS += ('raven.contrib.django.raven_compat',)
except ImportError:
    pass

# minimum logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'sentry': {
            'level': 'WARNING',
            'class': 'raven.contrib.django.raven_compat.handlers.SentryHandler',
        },
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        },
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'pensieve': {
            'handlers': ['sentry'],
            'level': 'WARNING',
        },
    }
}

EDIT_GENERALI_BASEPATH = '/www/edit_generali'
KCFEEDS_BASEPATH = '/www/siti/www.quotidiano.net/htdocs/djangomedia/kcfeeeds'
ALLOWED_INCLUDE_ROOTS = (
    EDIT_GENERALI_BASEPATH,
    KCFEEDS_BASEPATH,
)
