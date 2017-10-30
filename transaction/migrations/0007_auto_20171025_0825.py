# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0006_transaction_account'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='percentage',
            field=models.CharField(max_length=3),
        ),
    ]
