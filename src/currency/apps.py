import asyncio
from django.apps import AppConfig
from currency.index import worker1
# from currency.models import Value


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

# подключаемся к потоку
loop = asyncio.get_running_loop()
loop.create_task(worker1())
