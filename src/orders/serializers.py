from rest_framework import serializers
from .models import Order

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = ('pk', 'order_number', 'price_usd', 'price_rub', 'delivery_time')