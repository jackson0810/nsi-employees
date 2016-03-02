# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0007_auto_20160301_1656'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='commonfields',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='commonfields',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='functionalcapability',
            name='commonfields_ptr',
        ),
        migrations.RemoveField(
            model_name='imageitem',
            name='commonfields_ptr',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='commonfields_ptr',
        ),
        migrations.RemoveField(
            model_name='taskorder',
            name='commonfields_ptr',
        ),
        migrations.DeleteModel(
            name='CommonFields',
        ),
        migrations.DeleteModel(
            name='FunctionalCapability',
        ),
        migrations.DeleteModel(
            name='ImageItem',
        ),
        migrations.DeleteModel(
            name='NewsItem',
        ),
        migrations.DeleteModel(
            name='TaskOrder',
        ),
    ]
