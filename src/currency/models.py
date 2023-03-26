from django.db.models import Model, DecimalField

# Create your models here.


class Value(Model):
    usd = DecimalField(
        "Kурc USD", max_digits=7, decimal_places=4)

    def __str__(self):
        return self.usd

    class Meta:
        verbose_name = "Kурc"
        verbose_name_plural = "Курсы"
        db_table_comment = "Таблица для обновления курса валют"
