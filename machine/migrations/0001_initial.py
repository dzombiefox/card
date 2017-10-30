# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Machine',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('machineName', models.CharField(max_length=15, verbose_name='Machine Name')),
                ('bankRate', models.CharField(max_length=25, verbose_name='Bank Rate')),
                ('maxUsage', models.CharField(max_length=25, verbose_name='Maximum Usage')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
