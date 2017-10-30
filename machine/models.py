from __future__ import unicode_literals
from django.db import models



#Create your models here.
class Machine(models.Model):
    machineName = models.CharField(max_length=15,verbose_name="Machine Name")
    bankRate = models.CharField(max_length=25,verbose_name="Bank Rate")
    maxUsage = models.CharField(max_length=25, verbose_name="Maximum Usage")
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return  self.machineName
