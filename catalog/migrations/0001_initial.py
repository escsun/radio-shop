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
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=254, db_index=True, verbose_name='Имя')),
                ('image', models.ImageField(upload_to='category', verbose_name='Изображение', null=True, blank=True)),
                ('position', models.PositiveIntegerField(verbose_name='Позиция', default=0)),
                ('lft', models.PositiveIntegerField(db_index=True, editable=False)),
                ('rght', models.PositiveIntegerField(db_index=True, editable=False)),
                ('tree_id', models.PositiveIntegerField(db_index=True, editable=False)),
                ('level', models.PositiveIntegerField(db_index=True, editable=False)),
                ('parent', mptt.fields.TreeForeignKey(verbose_name='Категория', related_name='children', blank=True, null=True, to='catalog.Category')),
            ],
            options={
                'verbose_name_plural': 'Категории',
                'verbose_name': 'Категорию',
            },
        ),
        migrations.CreateModel(
            name='Name',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=32, unique=True, verbose_name='Наименование')),
            ],
            options={
                'verbose_name_plural': 'Наименования',
                'verbose_name': 'Наименование',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=254, verbose_name='Базовое имя')),
                ('name_values', models.CharField(max_length=254, verbose_name='Имя')),
                ('price', models.FloatField(verbose_name='Цена', null=True, blank=True)),
                ('description', models.CharField(max_length=254, verbose_name='Описание', null=True, blank=True)),
                ('code', models.CharField(max_length=32, verbose_name='Код товара', null=True, blank=True)),
                ('is_available', models.BooleanField(verbose_name='В наличие', default=True)),
                ('position', models.IntegerField(verbose_name='Позиция')),
                ('category', mptt.fields.TreeForeignKey(verbose_name='Категория', related_name='cat', blank=True, null=True, to='catalog.Category')),
            ],
            options={
                'verbose_name_plural': 'Товары',
                'verbose_name': 'Товар',
            },
        ),
        migrations.CreateModel(
            name='Value',
            fields=[
                ('id', models.AutoField(auto_created=True, verbose_name='ID', serialize=False, primary_key=True)),
                ('value', models.CharField(max_length=64, verbose_name='Значение', null=True)),
                ('visible', models.BooleanField(verbose_name='Отображать', default=1)),
                ('name', models.ForeignKey(verbose_name='Наименование', to='catalog.Name')),
                ('product', models.ForeignKey(verbose_name='Товар', null=True, to='catalog.Product')),
            ],
            options={
                'verbose_name_plural': 'Характеристики',
                'verbose_name': 'Характерстика',
            },
        ),
    ]
