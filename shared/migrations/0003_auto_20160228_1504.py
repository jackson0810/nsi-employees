# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0002_auto_20160225_1232'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='functionalcapability',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='newsitem',
            options={'ordering': ['title']},
        ),
        migrations.AlterModelOptions(
            name='taskorder',
            options={'ordering': ['task_number']},
        ),
        migrations.RemoveField(
            model_name='taskorder',
            name='document_name',
        ),
        migrations.AddField(
            model_name='taskorder',
            name='document',
            field=models.FileField(default='', upload_to='documents'),
            preserve_default=False,
        ),
    ]
