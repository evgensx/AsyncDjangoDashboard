from django.db import models

# Create your models here.


class Order(models.Model):
    id = models.CharField('ID', primary_key=True)
    order_number = models.CharField("Номер заказа", max_length=10)
    price_usd = models.DecimalField(
        "Стоимость, $", max_digits=8, decimal_places=2)
    price_rub = models.DecimalField(
        "Стоимость, \u20bd", max_digits=8, decimal_places=2)
    delivery_time = models.DateField("Срок поставки")

    def __str__(self):
        return self.order_number

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        
