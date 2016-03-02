# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shared', '0011_auto_20160301_1924'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactItem',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('first_name', models.CharField(max_length=100, verbose_name='First Name')),
                ('last_name', models.CharField(max_length=100, verbose_name='Last Name')),
                ('email', models.EmailField(max_length=250, db_index=True)),
                ('message', models.TextField(blank=True, null=True)),
                ('category', models.CharField(max_length=30)),
            ],
        ),
    ]
