from __future__ import unicode_literals
from django.db import models

#Create your models here.
class Customer(models.Model):
    date = models.DateField()
    identityNumber = models.CharField(max_length=15,verbose_name="Identity Number")
    customerName = models.CharField(max_length=25,verbose_name="Customer Name")
    dateBirth = models.DateField()
    contactNumber = models.CharField(max_length=25,verbose_name="Contact Name")
    handphone = models.CharField(max_length=15,verbose_name="No Handphone")
    email = models.CharField(max_length=25,verbose_name="Email")
    imagescan = models.ImageField(upload_to='prof_pic/',null=True,blank=True)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.machineName
