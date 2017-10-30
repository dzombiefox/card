from django import forms
from .models import Transaction

class TransactionForm(forms.ModelForm):
    class Meta :
        model =Transaction
        fields=["date","amount","type","percentage","amountAccept","totalSettle","note","customer","machine","account"]
