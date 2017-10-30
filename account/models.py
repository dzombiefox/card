from __future__ import unicode_literals
from django.db import models
from customer .models import Customer

class Bank(models.Model):
    bankName = models.CharField(max_length=15,verbose_name="Name Bank")
    def __str__(self):
        return self.bankName
#Create your models here.
class Account(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer)
    bank = models.ForeignKey(Bank)
    accountNumber = models.CharField(max_length=25 , verbose_name="Account Number")
    accountOwner = models.CharField(max_length=25,verbose_name="Account Owner")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.accountNumber

class CreditCard(models.Model):
    date = models.DateField()
    customer = models.ForeignKey(Customer)
    bank = models.ForeignKey(Bank)
    cardNumber = models.CharField(max_length=25 , verbose_name="Card Number")
    cardOwner = models.CharField(max_length=25,verbose_name="Card Owner")
    expired = models.CharField(max_length=25)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.cardNumber

# class Tes(models.Model):
#     tesName = models.CharField(max_length=15,verbose_name="TES Bank")
#     def __str__(self):
#         return self.tesName

