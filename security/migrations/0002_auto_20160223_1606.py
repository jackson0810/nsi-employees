# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='first_name',
            field=models.CharField(default='', verbose_name='First Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='last_name',
            field=models.CharField(default='', verbose_name='Last Name', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='mobile_phone',
            field=models.CharField(default='', verbose_name='mobile phone', max_length=14),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='customuser',
            name='office_phone',
            field=models.CharField(default='', verbose_name='office phone', max_length=14),
            preserve_default=False,
        ),
    ]
