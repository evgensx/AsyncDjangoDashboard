from django.contrib import admin

# Register your models here.
from .models import ExangeRate

@admin.register(ExangeRate)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'currency', 'value')
    list_display_links = ('id', 'currency',)
