# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0010_imageitem_featured'),
    ]

    operations = [
        migrations.AlterField(
            model_name='imageitem',
            name='featured',
            field=models.BooleanField(verbose_name='is this a featured image', default=True),
        ),
    ]
