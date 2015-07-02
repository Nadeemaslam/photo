# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0003_auto_20150623_0902'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='description',
            field=models.TextField(max_length=200, blank=True),
        ),
    ]
