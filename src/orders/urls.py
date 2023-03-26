from django.urls import re_path, path
from .views import *

urlpatterns = [
    path(r'', orders_list),
    re_path(r'^(\d+)$', order_detail),
]