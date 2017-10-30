from __future__ import unicode_literals
from django.db import models
from customer .models import Customer
from account .models import CreditCard,Account
from machine .models import Machine
from django.contrib.auth.models import User
#Create your models here.
class Transaction(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer)
    credit =models.ForeignKey(CreditCard)
    amount = models.CharField(max_length=15)
    type = models.CharField(max_length=15)
    percentage = models.CharField(max_length=3)
    account = models.ForeignKey(Account)
    amountAccept = models.IntegerField()
    totalSettle = models.IntegerField()
    machine = models.ForeignKey(Machine)
    note = models.TextField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    posted_by = models.ForeignKey(User)

    def __str__(self):
        return  self.date