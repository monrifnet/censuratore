# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pensieve', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='censura',
            name='title',
            field=models.CharField(max_length=100, verbose_name=b'titolo', blank=True),
        ),
    ]
