from django.db.models import Model, DecimalField, CharField

# Create your models here.
class ExangeRate(Model):
    currency = CharField("Валюта", max_length=5)
    value = DecimalField("Kурc валюты", max_digits=7, decimal_places=4)
    
    def __str__(self):
        return str(self.value)

    class Meta:
        verbose_name = "Kурc"
        verbose_name_plural = "Курсы"
        db_table_comment = "Таблица для обновления курса валют"
