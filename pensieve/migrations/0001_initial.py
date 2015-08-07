# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import django.db.models.deletion
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivioUrl',
            fields=[
                ('url', models.URLField(primary_key=True, serialize=False, editable=False, unique=True, verbose_name=b'URL')),
                ('created_time', models.DateTimeField(auto_now_add=True)),
                ('contents', models.TextField(verbose_name=b'contenuto', null=True, editable=False, blank=True)),
                ('screenshot', models.CharField(max_length=255, null=True, editable=False, blank=True)),
                ('censored_time', models.DateTimeField(null=True, blank=True)),
                ('censored_by', models.ForeignKey(related_name='censored_urls', on_delete=django.db.models.deletion.SET_NULL, blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('created_by', models.ForeignKey(related_name='created_urls', on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Censura',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(default='(senza titolo)', max_length=100, verbose_name=b'titolo')),
                ('ins_time', models.DateTimeField(auto_now_add=True, verbose_name=b'data inserimento')),
                ('mod_time', models.DateTimeField(auto_now=True, verbose_name=b'data modifica')),
                ('url_list', models.TextField(help_text='Inserisci uno o pi\xf9 URL separati da un "a capo"', verbose_name=b'URL da archiviare')),
                ('request_date', models.DateField(verbose_name=b'richiesto il')),
                ('request_by', models.CharField(max_length=100, verbose_name=b'richiesto da')),
                ('reason', models.TextField(verbose_name=b'motivazione/note')),
                ('operated_by', models.ForeignKey(related_name='censor_tasks', on_delete=django.db.models.deletion.SET_NULL, blank=True, editable=False, to=settings.AUTH_USER_MODEL, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='archiviourl',
            name='created_in',
            field=models.ForeignKey(related_name='task_urls', on_delete=django.db.models.deletion.SET_NULL, blank=True, to='pensieve.Censura', null=True),
        ),
    ]
