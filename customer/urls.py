from django.conf.urls import url
from . import views
from views import (index,add,edit,view)

urlpatterns = [
    url(r'^$', index, name="customer"),
    url(r'^add', add, name="addcustomer"),
    url(r'^edit/(?P<data>.+)$', views.edit, name="editcustomer"),
    url(r'^view/(?P<data>.+)$', views.view, name="viewcustomer"),
]