# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shared.utilities
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shared', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommonFields',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, verbose_name='ID', primary_key=True)),
                ('is_active', models.BooleanField(default=True)),
                ('dt_created', models.DateTimeField(auto_now_add=True)),
                ('dt_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='functionalcapability',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='functionalcapability',
            name='dt_created',
        ),
        migrations.RemoveField(
            model_name='functionalcapability',
            name='dt_updated',
        ),
        migrations.RemoveField(
            model_name='functionalcapability',
            name='id',
        ),
        migrations.RemoveField(
            model_name='functionalcapability',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='imageitem',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='imageitem',
            name='dt_created',
        ),
        migrations.RemoveField(
            model_name='imageitem',
            name='dt_updated',
        ),
        migrations.RemoveField(
            model_name='imageitem',
            name='id',
        ),
        migrations.RemoveField(
            model_name='imageitem',
            name='updated_by',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='created_by',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='dt_created',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='dt_updated',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='id',
        ),
        migrations.RemoveField(
            model_name='newsitem',
            name='updated_by',
        ),
        migrations.CreateModel(
            name='TaskOrder',
            fields=[
                ('commonfields_ptr', models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, to='shared.CommonFields', serialize=False)),
                ('task_uuid', models.CharField(db_index=True, default=shared.utilities.make_uuid, max_length=36)),
                ('task_number', models.CharField(max_length=100)),
                ('text', models.TextField()),
                ('document_name', models.CharField(max_length=250)),
            ],
            bases=('shared.commonfields',),
        ),
        migrations.AddField(
            model_name='commonfields',
            name='created_by',
            field=models.ForeignKey(related_name='created_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='commonfields',
            name='updated_by',
            field=models.ForeignKey(related_name='updated_by', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='functionalcapability',
            name='commonfields_ptr',
            field=models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, default='', to='shared.CommonFields', serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='imageitem',
            name='commonfields_ptr',
            field=models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, default='', to='shared.CommonFields', serialize=False),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsitem',
            name='commonfields_ptr',
            field=models.OneToOneField(primary_key=True, parent_link=True, auto_created=True, default='', to='shared.CommonFields', serialize=False),
            preserve_default=False,
        ),
    ]
