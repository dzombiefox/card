# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('identityNumber', models.CharField(max_length=15, verbose_name='Identity Number')),
                ('customerName', models.CharField(max_length=25, verbose_name='Customer Name')),
                ('dateBirth', models.DateField()),
                ('contactName', models.CharField(max_length=25, verbose_name='Contact Name')),
                ('handphone', models.CharField(max_length=15, verbose_name='No Handphone')),
                ('email', models.CharField(max_length=25, verbose_name='Email')),
                ('imagescan', models.ImageField(upload_to='prof_pic/', null=True, verbose_name='Scan', blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
