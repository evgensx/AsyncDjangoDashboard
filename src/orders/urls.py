from django.urls import re_path
from . import views

urlpatterns = [
    re_path(r'^$', views.orders_list),
    re_path(r'^(\d+)$', views.order_detail),
]