# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20171023_0146'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('accountNumber', models.CharField(max_length=25, verbose_name='Account Number')),
                ('accountOwner', models.CharField(max_length=25, verbose_name='Account Owner')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Bank',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('bankName', models.CharField(max_length=15, verbose_name='Name Bank')),
            ],
        ),
        migrations.CreateModel(
            name='CreditCard',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('cardNumber', models.CharField(max_length=25, verbose_name='Card Number')),
                ('cardOwner', models.CharField(max_length=25, verbose_name='Card Owner')),
                ('expired', models.DateField(null=True, blank=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('bank', models.ForeignKey(to='account.Bank')),
                ('customer', models.ForeignKey(to='customer.Customer')),
            ],
        ),
        migrations.AddField(
            model_name='account',
            name='bank',
            field=models.ForeignKey(to='account.Bank'),
        ),
        migrations.AddField(
            model_name='account',
            name='customer',
            field=models.ForeignKey(to='customer.Customer'),
        ),
    ]
