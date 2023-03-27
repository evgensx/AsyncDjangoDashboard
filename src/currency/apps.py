import asyncio
from django.apps import AppConfig
from currency.runner import worker1


# async def update_rate(obj):
#     k = 1.3456
#     while True:
#         rate = await obj.objects.aupdate_or_create(currency='usd', defaults={'value': k})
#         k+=1.0
#         print(rate)
#         print(type(obj))
#         await asyncio.sleep(1)


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'
    verbose_name = 'Курсы'


    def ready(self):
        from .models import ExangeRate
        # await update_rate(ExangeRate)
        loop = asyncio.get_running_loop()
        loop.create_task(worker1(ExangeRate))


# # подключаемся к потоку
# loop = asyncio.get_running_loop()
# loop.create_task(worker1())
