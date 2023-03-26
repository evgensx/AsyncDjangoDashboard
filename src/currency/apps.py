import asyncio
from django.apps import AppConfig
from currency.runner import worker1


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'
    verbose_name = 'Курсы'

# подключаемся к потоку
loop = asyncio.get_running_loop()
loop.create_task(worker1())
