# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='albums',
        ),
        migrations.RemoveField(
            model_name='image',
            name='created',
        ),
        migrations.RemoveField(
            model_name='image',
            name='height',
        ),
        migrations.RemoveField(
            model_name='image',
            name='image',
        ),
        migrations.RemoveField(
            model_name='image',
            name='rating',
        ),
        migrations.RemoveField(
            model_name='image',
            name='tags',
        ),
        migrations.RemoveField(
            model_name='image',
            name='title',
        ),
        migrations.RemoveField(
            model_name='image',
            name='user',
        ),
        migrations.RemoveField(
            model_name='image',
            name='width',
        ),
    ]
