# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0004_auto_20171017_0134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='imagescan',
            field=models.ImageField(null=True, upload_to='prof_pic/', blank=True),
        ),
    ]
