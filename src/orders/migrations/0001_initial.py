# Generated by Django 4.2rc1 on 2023-03-24 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.CharField(primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=10, verbose_name='Номер заказа')),
                ('price_usd', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость, $')),
                ('price_rub', models.DecimalField(decimal_places=2, max_digits=8, verbose_name='Стоимость, ₽')),
                ('delivery_time', models.DateField(verbose_name='Срок поставки')),
            ],
        ),
    ]