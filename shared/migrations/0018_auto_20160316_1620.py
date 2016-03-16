# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared', '0017_auto_20160306_1337'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', primary_key=True, serialize=False)),
                ('is_active', models.BooleanField(default=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('category', models.CharField(max_length=250, verbose_name='form category')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='formdata',
            name='category',
            field=models.ManyToManyField(to='shared.FormCategory'),
        ),
    ]
