from django.contrib import admin
from .models import Order

@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    # readonly_fields = ('id',)
    list_display = ('id', 'order_number', 'price_usd', 'price_rub', 'delivery_time')
    list_display_links = ('order_number', 'id')
    search_fields = ('order_number',)
