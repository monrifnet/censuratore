# -*- coding=utf-8 -*-
from settings import *

DEBUG = False
TEMPLATE_DEBUG = DEBUG

STATIC_URL = "http://www.stqn.it/djstatic/censuratore/"
NUHP_STATIC_URL = "http://www.stqn.it/nuhp_static"
STATIC_ROOT = "/www/siti/stqn/htdocs/djstatic/censuratore"
MEDIA_URL = "http://www.quotidiano.net/djangomedia/censuratore/"
MEDIA_ROOT = "/www/siti/www.quotidiano.net/htdocs/djangomedia/censuratore"

SITE_DOMAIN = 'http://www.quotidiano.net'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'censuratore',
        'HOST': '192.168.21.52',
        'USER': 'braghettone',
        'PASSWORD': 'diVolt3rra',
    }
}
