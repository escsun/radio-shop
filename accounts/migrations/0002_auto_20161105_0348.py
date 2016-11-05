# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings
import django.contrib.auth.models


class Migration(migrations.Migration):

    dependencies = [
        ('auth', '0006_require_contenttypes_0002'),
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(serialize=False, auto_created=True, verbose_name='ID', primary_key=True)),
                ('activation_key', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
            ],
            options={
                'proxy': True,
                'verbose_name': 'Группа',
                'verbose_name_plural': 'Группы',
            },
            bases=('auth.group',),
            managers=[
                ('objects', django.contrib.auth.models.GroupManager()),
            ],
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254, unique=True, verbose_name='email address', error_messages={'unique': 'Пользователь с таким электронным адресом уже существует.'}),
        ),
        migrations.AlterUniqueTogether(
            name='user',
            unique_together=set([]),
        ),
        migrations.AddField(
            model_name='profile',
            name='user',
            field=models.ForeignKey(related_name='profile', to=settings.AUTH_USER_MODEL),
        ),
    ]
