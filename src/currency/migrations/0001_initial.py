# Generated by Django 4.2rc1 on 2023-03-26 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ExangeRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('currency', models.CharField(max_length=5, verbose_name='Валюта')),
                ('value', models.DecimalField(decimal_places=4, max_digits=7, verbose_name='Kурc валюты')),
            ],
            options={
                'verbose_name': 'Kурc',
                'verbose_name_plural': 'Курсы',
                'db_table_comment': 'Таблица для обновления курса валют',
            },
        ),
    ]
