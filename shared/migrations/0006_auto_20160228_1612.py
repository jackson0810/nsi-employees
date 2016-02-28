# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0005_auto_20160228_1530'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='taskorder',
            name='text',
        ),
        migrations.AlterField(
            model_name='taskorder',
            name='document',
            field=models.FileField(upload_to='documents'),
        ),
    ]
