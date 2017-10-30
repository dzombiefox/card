from django.conf.urls import url
from . import views
from views import (index,add,edit)

urlpatterns = [
    url(r'^$', index, name="machine"),
    url(r'^add', add, name="addmachine"),
    # url(r'^getprice/(\d+)/(\d+)$',getprice,name="getprice"),
    # url(r'^save', save, name="saveJual"),
    url(r'^edit/(?P<dat>.+)$', views.edit, name="editmachine"),
    # url(r'^update',update,name="updateJual"),
    # url(r'^print/(?P<id>\d+)$', prints, name="print"),
    # url(r'^report', report, name="reportjual"),
    # url(r'^modalstok/(?P<id>\d+)$', modalstok, name="modalstok" ),
    # url

]