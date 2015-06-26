# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('photo', '0002_auto_20150623_0612'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='albums',
            field=models.ManyToManyField(to='photo.Album', blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='created',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='height',
            field=models.IntegerField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='image',
            field=models.ImageField(null=True, upload_to=b'images/'),
        ),
        migrations.AddField(
            model_name='image',
            name='rating',
            field=models.IntegerField(default=50),
        ),
        migrations.AddField(
            model_name='image',
            name='tags',
            field=models.ManyToManyField(to='photo.Tag', blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.CharField(max_length=60, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='image',
            name='user',
            field=models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True),
        ),
        migrations.AddField(
            model_name='image',
            name='width',
            field=models.IntegerField(null=True, blank=True),
        ),
    ]
