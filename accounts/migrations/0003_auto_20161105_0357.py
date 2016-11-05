# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_auto_20161105_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(verbose_name='username', max_length=30, unique=True, help_text='Требуется, не больше 30 символов или меньше, латинские буквы, числа, знаки подчеркивания и дефис.', validators=[django.core.validators.RegexValidator('^[A-z0-9_-]+$', 'Логин может содержать только латинские буквы, числа, знаки подчеркивания и дефис. Ограничения не больше 30 символов или меньше.', 'invalid')], error_messages={'unique': 'A user with that username already exists.'}),
        ),
    ]
