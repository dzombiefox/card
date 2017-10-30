from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .forms import AccountForm
from django.http import HttpResponseRedirect
from .models import Account,CreditCard
from django.utils.datastructures import MultiValueDictKeyError

@login_required
def index(request):
    return HttpResponse("BANGKE")

@login_required
def save(request):
    if request.POST:
        customer = request.POST['customer_id']
        date = request.POST['date']
        bank = request.POST['bank']
        account = request.POST['accountNumber']
        owner = request.POST['accountOwner']
        account= Account(customer_id=customer,date=date,accountNumber=account,accountOwner=owner,bank_id=bank)
        account.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

@login_required
def simpancard(request):
    if request.POST:
        customer = request.POST['customer_id']
        date = request.POST['date']
        bank = request.POST['bank']
        cardnumber = request.POST['cardNumber']
        cardowner = request.POST['cardOwner']
        expired = request.POST['expired']
        card = CreditCard(customer_id=customer,date=date,bank_id=bank,cardNumber=cardnumber,cardOwner=cardowner,expired=expired)
        card.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
