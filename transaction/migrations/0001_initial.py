# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_auto_20171023_0146'),
        ('account', '0004_auto_20171023_0219'),
        ('machine', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateField()),
                ('amount', models.IntegerField()),
                ('type', models.CharField(max_length=15)),
                ('percentage', models.CharField(max_length=3)),
                ('amountAccept', models.IntegerField()),
                ('totalSettle', models.IntegerField()),
                ('note', models.CharField(max_length=225)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('credit', models.ForeignKey(to='account.CreditCard')),
                ('customer', models.ForeignKey(to='customer.Customer')),
                ('machine', models.ForeignKey(to='machine.Machine')),
            ],
        ),
    ]
