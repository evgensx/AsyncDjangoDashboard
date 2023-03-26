from django.contrib import admin

# Register your models here.
from .models import Value

@admin.register(Value)
class OrderAdmin(admin.ModelAdmin):
    list_display = ('id', 'usd')
    list_display_links = ('id', 'usd',)
