# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0020_auto_20160317_1217'),
    ]

    operations = [
        migrations.AlterField(
            model_name='formdata',
            name='data_type',
            field=models.CharField(max_length=5),
        ),
    ]
