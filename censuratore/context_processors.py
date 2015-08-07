# -*- coding=utf-8 -*-
from django.conf import settings

def basepaths(request):
    return {
        'ssi_edit_generali': settings.EDIT_GENERALI_BASEPATH,
        'ssi_kcfeeds': settings.KCFEEDS_BASEPATH,
    }

def extra_static_paths(request):
    return {
        'nuhp_static': settings.NUHP_STATIC_URL,
    }
