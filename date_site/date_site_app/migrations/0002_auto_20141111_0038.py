# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('date_site_app', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='country',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='sity',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='birthday',
            field=models.DateField(default=datetime.datetime(9999, 12, 31, 0, 0), verbose_name=b'birthday'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='gender',
            field=models.CharField(max_length=1, choices=[(b'm', b'Male'), (b'f', b'Female')]),
        ),
    ]
