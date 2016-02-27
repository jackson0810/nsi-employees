# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('security', '0003_auto_20160223_1609'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='account_type',
            field=models.IntegerField(),
        ),
    ]
