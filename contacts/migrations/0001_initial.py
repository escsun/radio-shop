# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contacts',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(auto_now=True, verbose_name='Дата и время', auto_created=True)),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('message', models.TextField(verbose_name='Сообщение')),
            ],
            options={
                'verbose_name_plural': 'Сообщения',
                'verbose_name': 'Сообщение',
            },
        ),
    ]
