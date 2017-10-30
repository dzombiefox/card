from django.conf.urls import url
from . import views
from views import (index,create,saveidentity,savecard,printinvoice,edit)

urlpatterns = [
    url(r'^$', index, name="transaction"),
    url(r'^create', create, name="createTransaction"),
    url(r'^saveidentity', saveidentity, name="saveidentity"),
    url(r'^savecard', savecard, name="savecard"),
    url(r'^edit/(?P<dat>.+)$', views.edit, name="edittransaction"),
    url(r'^printinvoice/(?P<id>.+)$', views.printinvoice, name="printinvoice"),
]