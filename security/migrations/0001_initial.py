# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import shared.utilities


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, primary_key=True, auto_created=True)),
                ('password', models.CharField(verbose_name='password', max_length=128)),
                ('last_login', models.DateTimeField(verbose_name='last login', blank=True, null=True)),
                ('username', models.CharField(verbose_name='User Name', null=True, blank=True, max_length=250)),
                ('user_uuid', models.CharField(default=shared.utilities.make_uuid, db_index=True, max_length=36)),
                ('account_type', models.IntegerField(choices=[(1, 'Administrator'), (2, 'General User'), (3, 'News Admin')])),
                ('email', models.EmailField(unique=True, db_index=True, max_length=250)),
                ('password_reset', models.BooleanField(default=False)),
                ('is_active', models.BooleanField(default=False, verbose_name='Is Active')),
                ('is_admin', models.BooleanField(default=False, verbose_name='Is Superuser', help_text='Django admin user.')),
                ('dt_created', models.DateTimeField(verbose_name='Date/Time Created', auto_now_add=True)),
                ('dt_updated', models.DateTimeField(verbose_name='Date/Time Updated', auto_now=True)),
                ('dt_last_login', models.DateTimeField(verbose_name='Date/Time Last Login', blank=True, null=True)),
                ('dt_password_reset', models.DateTimeField(verbose_name='Date/Time Password Reset', blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Users',
                'verbose_name': 'User',
                'ordering': ['email'],
            },
        ),
        migrations.AlterUniqueTogether(
            name='customuser',
            unique_together=set([('email', 'account_type')]),
        ),
    ]
