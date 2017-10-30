from __future__ import unicode_literals
from django.http import HttpResponse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from machine .models import Machine
from .forms import MachineForm
from functions.functions import decript
@login_required
def index(request):
    data = Machine.objects.all()
    return render(request,"machine/index.html",{"data":data})

@login_required
def add(request):
    if request.POST:
        form = MachineForm(request.POST)
        if form.is_valid():
            if form.save():
                return redirect('machine')
            else:
                return HttpResponse("No oke")
        else:
            return HttpResponse("form failed")
    else :
        form = MachineForm()
        return render(request,"machine/add.html",{"form":form})


@login_required
def edit(request,dat):
    if request.POST:
        id= decript(dat)
        data = Machine.objects.get(id=id)
        form = MachineForm(request.POST,instance=data)
        form.save()
        return redirect("machine")
    else :
        id = decript(dat)
        data = Machine.objects.get(id=id)
        form = MachineForm(instance=data)
        return render(request,"machine/edit.html",{"form":form})