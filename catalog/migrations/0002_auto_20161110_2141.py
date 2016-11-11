# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='value',
            options={'verbose_name_plural': 'Наименования', 'verbose_name': 'Наименование'},
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(null=True, blank=True, verbose_name='Изображение', upload_to='category'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(null=True, blank=True, verbose_name='Изображение', upload_to='product'),
        ),
    ]
