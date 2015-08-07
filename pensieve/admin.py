#-*-coding=UTF-8-*-
from django.contrib import admin
from pensieve.models import ArchivioUrl,Censura
from django.utils.html import format_html
import logging

logger = logging.getLogger(__name__)

class ArchivioUrlInline(admin.TabularInline):
    model = ArchivioUrl
    
    extra = 0
    can_delete = False
    
    readonly_fields = ('url', 'created_by', 'created_time', 'is_archived', 'is_censored')

class CensuraAdmin(admin.ModelAdmin):
    model = Censura
    
    list_display = ('title', 'operated_by', 'ins_time', 'mod_time', 'request_date', 'request_by', 'num_urls', 'cens_state', 'note')
    search_fields = ['title', 'operated_by', 'ins_time', 'mod_time', 'request_date', 'request_by', 'cens_state', 'note']
    
    inlines = [ ArchivioUrlInline, ]
    
    def num_urls(self, obj):
        urls = obj.get_all_urls()
        if urls:
            return len(urls)
        return 0
    num_urls.short_description = u'URL inseriti'
    
    def cens_state(self, obj):
        state = obj.get_censored_state()
        if state > 0:
            return True
        return False
    cens_state.short_description = u'URL archiviati'
    cens_state.boolean = True
    
    def note(self, obj):
        if obj.reason and len(obj.reason):
            return True
        return False
    note.boolean = True
    
    def sync_urls(self, request, obj, change):
        urls = obj.get_new_urls()
        for url_r in urls:
            url_obj = None
            try:
                url_obj = ArchivioUrl(url = url_r)
            except Exception as e:
                logger.error(e, exc_info=True)
                continue
            if url_obj:
                url_obj.created_by = request.user
                url_obj.created_in = obj
                url_obj.save()
    
    def save_model(self, request, obj, form, change):
        if not change:
            obj.operated_by = request.user
        obj.url_list = "\n".join(obj.get_all_urls())
        self.sync_urls(request, obj, change)
        super(self.__class__, self).save_model(request, obj, form, change)

admin.site.register(Censura, CensuraAdmin)
