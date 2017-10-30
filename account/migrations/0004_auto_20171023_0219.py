# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0003_auto_20171023_0218'),
    ]

    operations = [
        migrations.AlterField(
            model_name='creditcard',
            name='expired',
            field=models.CharField(max_length=25),
        ),
    ]
