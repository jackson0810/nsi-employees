# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('external', '0002_auto_20160221_1155'),
    ]

    operations = [
        migrations.CreateModel(
            name='FunctionalCapability',
            fields=[
                ('id', models.AutoField(primary_key=True, verbose_name='ID', serialize=False, auto_created=True)),
                ('title', models.CharField(verbose_name='title of functional capability', max_length=250)),
                ('text', models.TextField(verbose_name='detail')),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
                ('created_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='func_created_by')),
                ('updated_by', models.ForeignKey(to=settings.AUTH_USER_MODEL, related_name='func_updated_by')),
            ],
        ),
        migrations.AlterField(
            model_name='imageitem',
            name='text',
            field=models.TextField(verbose_name='image detail'),
        ),
        migrations.AlterField(
            model_name='imageitem',
            name='title',
            field=models.CharField(verbose_name='title of image item', max_length=250),
        ),
        migrations.AlterField(
            model_name='newsitem',
            name='text',
            field=models.TextField(verbose_name='news detail'),
        ),
    ]
