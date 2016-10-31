# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product/no-image.png', verbose_name='Изображение', upload_to='product'),
        ),
        migrations.AlterField(
            model_name='category',
            name='image',
            field=models.ImageField(default='category/no-image.png', verbose_name='Изображение', upload_to='category'),
        ),
    ]
