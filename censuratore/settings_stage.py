# -*- coding=utf-8 -*-
from settings import *

SITE_DOMAIN = 'http://test.quotidiano.net'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': '/home/uwsgi/_db/censuratore.db',
    }
}
STATIC_URL = "http://www.stqn.it/djstatic/censuratore_stage/"
NUHP_STATIC_URL = "http://www.stqn.it/stage/nuhp_static"
STATIC_ROOT = "/www/siti/stqn/htdocs/djstatic/censuratore_stage"
MEDIA_URL = "http://www.quotidiano.net/djangomedia/censuratore_stage/"
MEDIA_ROOT = "/www/siti/www.quotidiano.net/htdocs/djangomedia/censuratore_stage"
NEWRELIC_INI_PATH = '/home/uwsgi/censuratore/censuratore/newrelic.ini'

CELERY_RESULT_BACKEND = 'cache+memcached://192.168.21.55:11211/'
BROKER_URL = 'amqp://guest:guest@192.168.21.51:5672//'
CELERY_DEFAULT_QUEUE = 'censuratore-stage'
from kombu import Exchange, Queue
CELERY_QUEUES = (
    Queue('censuratore-stage', Exchange('stage'), routing_key='censuratore'),
)

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
