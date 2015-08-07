# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pensieve', '0002_auto_20150729_1216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='censura',
            name='reason',
            field=models.TextField(verbose_name=b'motivazione/note', blank=True),
        ),
    ]
