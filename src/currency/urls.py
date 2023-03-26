from django.urls import re_path, path
from .views import *

urlpatterns = [
    path(r'', values_list),
    re_path(r'^(\d+)$', value_detail),
]