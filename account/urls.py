from django.conf.urls import url
from . import views
from views import (save,simpancard,index)

urlpatterns = [
    url(r'^$', index, name="account"),
    url(r'^save', save, name="saveaccount"),
    url(r'^simpancard', simpancard, name="simpancard"),
    # url(r'^edit/(?P<data>.+)$', views.edit, name="editcustomer"),
    # url(r'^view/(?P<data>.+)$', views.view, name="viewcustomer"),
]