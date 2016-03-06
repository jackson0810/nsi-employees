# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shared.utilities
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared', '0016_newsitem_news_year'),
    ]

    operations = [
        migrations.CreateModel(
            name='FormData',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('is_active', models.BooleanField(default=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('form_uuid', models.CharField(default=shared.utilities.make_uuid, db_index=True, max_length=36)),
                ('title', models.CharField(verbose_name='title of form', max_length=250)),
                ('text', models.TextField(null=True, verbose_name='form detail', blank=True)),
                ('document', models.FileField(upload_to='/vagrant/shared/static/forms')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='news_year',
            field=models.IntegerField(),
        ),
    ]
