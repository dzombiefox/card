from django import forms
from .models import Account,CreditCard


class CreditCardForm(forms.ModelForm):
    class Meta :
        model =CreditCard
        fields=["date","bank","cardNumber","cardOwner","expired"]

class AccountForm(forms.ModelForm):
    class Meta :
        model =Account
        fields=["date","bank","accountNumber","accountOwner"]
