# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0014_contactitem_contact_uuid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contactitem',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='contactitem',
            name='last_name',
        ),
        migrations.AddField(
            model_name='contactitem',
            name='name',
            field=models.CharField(max_length=100, verbose_name='Name', default=''),
            preserve_default=False,
        ),
    ]
