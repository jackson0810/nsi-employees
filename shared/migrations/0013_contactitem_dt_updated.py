# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.utils.timezone import utc
import datetime


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0012_contactitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactitem',
            name='dt_updated',
            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2016, 3, 2, 1, 46, 35, 122285, tzinfo=utc)),
            preserve_default=False,
        ),
    ]
