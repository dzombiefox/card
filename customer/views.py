from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import Customer
from .forms import CustomerForm
from django.contrib import messages
from django.http import HttpResponseRedirect
from functions .functions import decript
from account .forms import AccountForm,CreditCardForm
from account .models import Account,CreditCard
@login_required
def index(request):
    data = Customer.objects.all()
    return render(request,"customer/index.html",{"data":data})

@login_required
def add(request):
    if request.POST:
        form = CustomerForm(request.POST,request.FILES)
        if form.is_valid():
            if form.save():
                return redirect('customer')
            else:
                return HttpResponse("No oke")
        else:
            messages.add_message(request, messages.INFO, 'form submission success')
            return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else :
        form = CustomerForm()
        return render(request,"customer/add.html",{"form":form})

@login_required
def edit(request,data):
    if request.POST :
        form = CustomerForm(request.POST)
        if form.is_valid():
            data = Customer.objects.get(pk=decript(data))
            form = CustomerForm(request.POST, instance=data)
            form.save()
            data = Customer.objects.all()
            return render(request, "customer/index.html", {"data": data})
        else :
            return HttpResponse("FORM INVALID")
    else :
        id = decript(data)
        data = Customer.objects.get(id=id)
        form = CustomerForm(instance=data)
        return render(request, "customer/edit.html", {"form": form, "id": id})

@login_required
def view(request,data):
    id = decript(data)
    data = Customer.objects.get(id=id)
    form_a = AccountForm()
    form_b = CreditCardForm()
    account = Account.objects.filter(customer_id=id)
    card = CreditCard.objects.filter(customer_id=id)
    return render(request, "customer/view.html", {"data": data,"id":id,"form_a":form_a,"account":account,"form_b":form_b,"card":card})
    # return HttpResponse(decript(data))