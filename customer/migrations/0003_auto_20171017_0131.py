# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20171014_0408'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contactNumber',
            field=models.IntegerField(max_length=25, verbose_name='Contact Name'),
        ),
    ]
