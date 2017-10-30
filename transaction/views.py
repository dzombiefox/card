from django.shortcuts import render, redirect
from django.http import HttpResponse

from functions.functions import decript
from .forms import TransactionForm
from customer .models import Customer
from django.contrib import messages
from account .models import CreditCard
from django.http import HttpResponseRedirect
from .forms import TransactionForm
from transaction .models import Transaction
from account .models import Account
from functions import functions
from django.db.models import Q

# Create your views here.
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    data = Transaction.objects.all()
    return render(request,"transaction/index.html",{"data":data})

@login_required
def create(request):
    if request.POST:
        input = request.POST['input']
        filterCustomer = Customer.objects.filter(identityNumber=input)
        if filterCustomer.exists():
            data  = Customer.objects.get(identityNumber=input)
            form = TransactionForm()
            account = Account.objects.filter(customer__identityNumber=input)
            card = CreditCard.objects.filter(customer__identityNumber=input)
            trans = Transaction.objects.filter(customer__identityNumber=input)
            return render(request,"transaction/inputIdentity.html",{"data":data,"form":form,"card":card,"trans":trans,"account":account})

        else :
            filtercard = CreditCard.objects.filter(cardNumber=input)
            if filtercard.exists():
                trans = Transaction.objects.filter(customer__creditcard__cardNumber=input)
                data  = CreditCard.objects.get(cardNumber=input)
                form = TransactionForm()
                account = Account.objects.filter(customer__creditcard__cardNumber=input)
                return render(request, "transaction/inputcard.html",{"form":form,"data":data,"account":account,"trans":trans})
            else :
                messages.add_message(request, messages.INFO, 'form submission success')
                return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    else :

        return render(request,"transaction/add.html")

@login_required
def saveidentity(request):
    identitynumber =request.POST['identitynumber']
    user = request.POST['user']
    custommer = Customer.objects.get(identityNumber=identitynumber)
    custommer_id = custommer.id
    date = request.POST['date']
    credit = request.POST['credit']
    amount = request.POST['amount'].replace(',', '')
    type = request.POST['type']
    account = request.POST['account']
    percentage = request.POST['percentage']
    amountAccept = 0
    totalSettle = 0
    if int(type) == 0:
        totalSettle = amount
        amountAccept = (((100 - float(percentage)) / 100)* float(amount))
    else :
        amountAccept = amount
        totalSettle  =int((float(percentage)/100 * float(amount)) + float(amount))
    machine = request.POST['machine']
    note =request.POST['note']
    trans = Transaction(date = date,amount=amount,type=type,percentage=percentage,amountAccept=amountAccept,totalSettle=totalSettle,note=note,credit_id=credit,customer_id=custommer_id,machine_id=machine,account_id=account,posted_by_id = user)
    trans.save()
    data = Transaction.objects.all()
    return redirect('transaction')

@login_required
def savecard(request):
    custommer_id = request.POST['identitynumber']
    user = request.POST['user']
    date = request.POST['date']
    credit_id = request.POST['credit']
    card = CreditCard.objects.get(cardNumber=credit_id)
    credit=card.id
    amount = request.POST['amount'].replace(',', '')
    type = request.POST['type']
    account = request.POST['account']
    percentage = request.POST['percentage']
    amountAccept = 0
    totalSettle = 0
    if int(type) == 0:
        totalSettle = amount
        amountAccept = (((100 - float(percentage)) / 100) * float(amount))
    else:
        amountAccept = amount
        totalSettle = int((float(percentage) / 100 * float(amount)) + float(amount))
    machine = request.POST['machine']
    note =request.POST['note']
    trans = Transaction(date = date,amount=amount,type=type,percentage=percentage,amountAccept=amountAccept,totalSettle=totalSettle,note=note,credit_id=credit,customer_id=custommer_id,machine_id=machine,account_id=account,posted_by_id = user)
    trans.save()
    data = Transaction.objects.all()
    return redirect('transaction')

@login_required
def printinvoice(request,id):
    idnya = decript(id)
    data = Transaction.objects.get(id = idnya)
    return render(request,"transaction/print.html",{"data":data})

@login_required
def edit(request,dat):
    # return HttpResponse("BANGKE")

    if request.POST:
        # return HttpResponse("KOK")
        id = request.POST['id']
        date = request.POST['date']
        credit = request.POST['credit']
        amount = request.POST['amount'].replace(',', '')
        type = request.POST['type']
        account = request.POST['account']
        percentage = request.POST['percentage']
        amountAccept = 0
        totalSettle = 0
        if int(type) == 0:
            totalSettle = amount
            amountAccept = (((100 - float(percentage)) / 100) * float(amount))
        else:
            amountAccept = amount
            totalSettle = int((float(percentage) / 100 * float(amount)) + float(amount))
        machine = request.POST['machine']
        note = request.POST['note']
        Transaction.objects.filter(id=id).update(date = date, credit_id = credit , amount = amount ,account = account ,machine = machine , type = type,percentage =percentage , note = note ,totalSettle = totalSettle , amountAccept = amountAccept )
        return redirect("transaction")

    else :
        id = decript(dat)
        data = Transaction.objects.get(id=id)
        form = TransactionForm(instance=data)
        card = CreditCard.objects.filter(customer_id=data.customer_id)
        account = Account.objects.filter(customer_id=data.customer_id)
        trans = Transaction.objects.filter(~Q(id=id),customer_id=data.customer_id)
        return render(request,"transaction/edit.html",{"data":data,"form":form,"card":card,"account":account,"trans":trans})