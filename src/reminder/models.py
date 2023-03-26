from django.db import models

# Create your models here.
class User(models.Model):
    user_id = models.CharField("User ID", max_length=10)
    chat_id = models.CharField("Chat ID", max_length=10, blank=True)
    # reminder_id_list = models.CharField("", max_length=10)
    
    def __str__(self):
        return self.user_id
    
    class Meta:
        verbose_name = "Контакт"
        verbose_name_plural = "Контакты"

class Notification(models.Model):
    order_number = models.CharField("№ заказа", max_length=10)

    def __str__(self):
        return self.order_number
    
    class Meta:
        verbose_name = "Уведомление"
        verbose_name_plural = "Уведомления"