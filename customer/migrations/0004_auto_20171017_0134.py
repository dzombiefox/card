# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0003_auto_20171017_0131'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='contactNumber',
            field=models.CharField(max_length=25, verbose_name='Contact Name'),
        ),
    ]
