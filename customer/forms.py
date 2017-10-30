from django import forms
from .models import Customer

class CustomerForm(forms.ModelForm):
    class Meta :
        model =Customer
        fields=["date","identityNumber","customerName","dateBirth","contactNumber","handphone","email","imagescan"]