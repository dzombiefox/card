# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0004_auto_20171023_0219'),
        ('transaction', '0005_auto_20171024_1009'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaction',
            name='account',
            field=models.ForeignKey(default=1, to='account.Account'),
            preserve_default=False,
        ),
    ]
