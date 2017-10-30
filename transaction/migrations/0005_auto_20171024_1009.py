# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0004_auto_20171024_0811'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='note',
            field=models.TextField(max_length=200),
        ),
    ]
