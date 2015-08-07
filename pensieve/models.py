# -*- coding=utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import re

class ArchivioUrl(models.Model):
    url = models.URLField('URL', primary_key=True, editable=False, unique=True)
    created_by = models.ForeignKey(User, related_name='created_urls', null=True, blank=True, on_delete=models.SET_NULL, editable=False)
    created_time = models.DateTimeField(auto_now_add=True)
    created_in = models.ForeignKey('Censura', related_name='task_urls', null=True, blank=True, on_delete=models.SET_NULL)
    contents = models.TextField('contenuto', null=True, blank=True, editable=False)
    screenshot = models.CharField(null=True, blank=True, max_length=255, editable=False)
    censored_by = models.ForeignKey(User, related_name='censored_urls', null=True, blank=True, on_delete=models.SET_NULL)
    censored_time = models.DateTimeField(null=True, blank=True)
    
    def is_archived(self):
        if self.contents is not None:
            return True
        return False
    
    def is_censored(self):
        if self.censored_time:
            return True
        return False

class Censura(models.Model):
    title = models.CharField('titolo', max_length=100, blank=True)
    operated_by = models.ForeignKey(User, related_name='censor_tasks', null=True, blank=True, on_delete=models.SET_NULL, editable=False)
    ins_time = models.DateTimeField('data inserimento', auto_now_add=True)
    mod_time = models.DateTimeField('data modifica', auto_now=True)
    url_list = models.TextField('URL da archiviare', help_text=u'Inserisci uno o più URL separati da un "a capo"')
    request_date = models.DateField('richiesto il')
    request_by = models.CharField('richiesto da', max_length=100)
    reason = models.TextField('motivazione/note', blank=True)
    
    def get_urls(self):
        try:
            urls = ArchivioUrl.objects.filter(created_in=self).order_by('created_time')
        except Exception as e:
            urls = []
            logger.error(e, exc_info=True)
        return urls
    
    def get_text_urls(self):
        text_urls = []
        if self.url_list and len(self.url_list):
            text_urls = re.split("[\n\r]+", self.url_list)
            text_urls = filter(None, [x.strip(' ') for x in text_urls])
        return text_urls
    
    def get_all_urls(self):
        obj_urls = [x.url for x in self.get_urls()]
        text_urls = self.get_text_urls()
        all_urls = set(obj_urls + text_urls)
        return sorted(all_urls)
    
    def get_new_urls(self):
        all_urls = self.get_all_urls()
        obj_urls = [x.url for x in self.get_urls()]
        new_urls = [x for x in all_urls if x not in obj_urls]
        return new_urls
    
    def get_censored_state(self):
        # state -1 means some, but not all, URLs have been censored
        # state 0 means no URLs have been censored
        # state 1 means all URLs have been censored
        urls = self.get_urls()
        censored_num = 0
        urls_length = len(urls)
        if not urls_length:
            return 0
        for url in urls:
            if url.is_censored():
                censored_num += 1
        if censored_num == urls_length:
            return 1
        elif censored_num > 0:
            return -1
        return 0
