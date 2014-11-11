# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('date_site_app', '0002_auto_20141111_0038'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='birthday',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='date_of_birth',
            field=models.DateField(default=datetime.datetime(9999, 12, 31, 0, 0), verbose_name=b'date_of_birth'),
            preserve_default=True,
        ),
    ]
