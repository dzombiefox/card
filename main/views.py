from __future__ import unicode_literals
from django.shortcuts import render
from django.contrib.auth.decorators import login_required,permission_required
from django.http import HttpResponse,HttpResponseRedirect
import datetime
from django.shortcuts import redirect
# Create your views here.
from django.contrib.admin import forms
from django.contrib.auth.models import  Permission


@login_required
def index(request):
    user = request.user
    # form = forms.ProfileForm(instance=user.profile)
    # permission = Permission.objects.all()
    # users = User.objects.all()
    return render(request,"index.html")

