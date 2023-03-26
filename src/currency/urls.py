from django.urls import re_path, path
from .views import *

urlpatterns = [
    path(r'', rates_list),
    re_path(r'^(\d+)$', rate_detail),
    # path(r"edit/<int:id>/", rate_edit),
    path(r'edit/', current_datetime)
]