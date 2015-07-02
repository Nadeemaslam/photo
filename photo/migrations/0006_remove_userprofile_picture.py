# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photo', '0005_userprofile'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='picture',
        ),
    ]
