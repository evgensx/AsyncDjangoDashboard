from django.apps import AppConfig
from . import bot
import asyncio
# from .bot import main


class ReminderConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'reminder'
    verbose_name = 'Уведомления'
    
    # print('check1')
    
    
    # def ready(self) -> None:
    #     print('проверка 1')

# print('check2')

# if __name__ == '__main__':
#     # Execute broadcaster
    
#     executor.start(dp, broadcaster())