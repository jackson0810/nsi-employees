# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0006_auto_20160228_1612'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='imageitem',
            name='featured',
        ),
        migrations.AlterField(
            model_name='imageitem',
            name='image',
            field=models.ImageField(default='', upload_to='/vagrant/shared/static/img/featured'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='imageitem',
            name='text',
            field=models.TextField(blank=True, verbose_name='image detail', null=True),
        ),
        migrations.AlterField(
            model_name='taskorder',
            name='document',
            field=models.FileField(upload_to='/vagrant/shared/static/documents'),
        ),
    ]
