# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import mptt.fields


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Имя', max_length=254, db_index=True)),
                ('image', models.ImageField(default='category/no-image.png', upload_to='category', verbose_name='Изображение')),
                ('position', models.PositiveIntegerField(default=0, verbose_name='Позиция')),
                ('lft', models.PositiveIntegerField(editable=False, db_index=True)),
                ('rght', models.PositiveIntegerField(editable=False, db_index=True)),
                ('tree_id', models.PositiveIntegerField(editable=False, db_index=True)),
                ('level', models.PositiveIntegerField(editable=False, db_index=True)),
                ('parent', mptt.fields.TreeForeignKey(null=True, related_name='children', to='catalog.Category', verbose_name='Категория', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категорию',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Наименование', max_length=32, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Наименования',
                'verbose_name': 'Наименование',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('name', models.CharField(verbose_name='Базовое имя', max_length=254)),
                ('name_values', models.CharField(verbose_name='Имя', max_length=254)),
                ('price', models.FloatField(null=True, verbose_name='Цена', blank=True)),
                ('code', models.CharField(null=True, verbose_name='Код товара', max_length=32, blank=True)),
                ('is_available', models.BooleanField(default=True, verbose_name='В наличие')),
                ('image', models.ImageField(default='product/no-image.png', upload_to='product', verbose_name='Изображение')),
                ('position', models.PositiveIntegerField(default=10, verbose_name='Позиция')),
                ('category', mptt.fields.TreeForeignKey(null=True, related_name='cat', to='catalog.Category', verbose_name='Категория', blank=True)),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(verbose_name='ID', auto_created=True, primary_key=True, serialize=False)),
                ('value', models.CharField(null=True, verbose_name='Значение', max_length=64)),
                ('visible', models.BooleanField(default=1, verbose_name='Отображать')),
                ('name', models.ForeignKey(to='catalog.Name', verbose_name='Наименование')),
                ('product', models.ForeignKey(null=True, to='catalog.Product', verbose_name='Товар')),
            ],
            options={
                'verbose_name_plural': 'Характеристики',
                'verbose_name': 'Характерстика',
            },
        ),
    ]
