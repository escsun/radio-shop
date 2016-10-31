# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_remove_product_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='position',
            field=models.PositiveIntegerField(default=10, verbose_name='Позиция'),
        ),
    ]
