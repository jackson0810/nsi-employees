# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0002_auto_20160223_1606'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='mobile_phone',
            field=models.CharField(verbose_name='mobile phone', max_length=14, null=True, blank=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='office_phone',
            field=models.CharField(verbose_name='office phone', max_length=14, null=True, blank=True),
        ),
    ]
