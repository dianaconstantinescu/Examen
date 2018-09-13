from django.conf.urls import url
from django.urls import path, re_path

from . import views

app_name = 'orders'

urlpatterns = [
    re_path('^$', views.order_complete, name='order_complete'),
]