import asyncio
# import concurrent.futures
from asgiref.sync import sync_to_async
import aiohttp
import datetime
import xml.etree.ElementTree as ET
import logging

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")
# import django
# django.setup()
from currency.models import Value

from os import environ
from dotenv import load_dotenv


load_dotenv()

logging.basicConfig(level=logging.INFO)
log = logging.getLogger('usd_exchange_rate')

# константа в какой час обновлять курс валюты
UPDATE_TIME = int(environ['UPDATE_TIME'])

date_today = datetime.date.today().strftime("%d/%m/%Y")
cbr_url = 'https://www.cbr.ru/scripts/XML_daily.asp?date_req=' + date_today


# async def update_exange_rate():  # *args, **kwargs
#     usd_rate = models.Value.objects.aget()
#     print(usd_rate)
    # await usd_rate.asave(using="secondary")


async def fetch_xml(session, url):
    async with session.get(url) as response:
        result = await response.text()
        # print(result)
        return result


@sync_to_async
def parse_xml(xml_data):
    # loop = asyncio.get_running_loop()
    root = ET.fromstring(xml_data)

    # do something with the parsed XML data
    for valute in root.findall('Valute'):
        if valute.get('ID') == "R01235":
            value = valute.find('Value')
            assert value is not None
            value = value.text
            return value


async def get_value():
    """
    Получение курса доллара к рублю
    """
    async with aiohttp.ClientSession() as session:
        # делаем запрос страницы xml
        xml_data = await fetch_xml(session, cbr_url)
        # парсим
        parsed_xml = await parse_xml(xml_data)
        # вызываем функцию записи в бд
        print(parsed_xml)


async def worker1():
    # await update_exange_rate()
    """
    Воркер проверяющий курс ЦБР каждый день
    """
    # получаем время запуска воркера
    run_time = datetime.datetime.now()
    # выполняем функцию получения курса валюты
    week_day = run_time.weekday
    await get_value()
    if week_day == 5:
        day = 3
    elif week_day == 6:
        day = 2
    else:
        day = 1
    # получаем время когда нужно продолжить выполнение воркера
    set_time = day * 3600 * (24 - run_time.hour + UPDATE_TIME) - (60 * run_time.minute)
    # отправляем спать воркер
    await asyncio.sleep(set_time)
    while True:
        logging.info('Worker 1 is running')
        # текущее время
        now_time = datetime.datetime.now()
        # т.к. курс обновляется только по будням, выбираем с понедельника по четверг и установленное время
        if now_time.weekday() in [7, 1, 2, 3, 4] and now_time.hour == UPDATE_TIME:
            # получение курса
            await get_value()
            logging.info('Получено значение курса доллара к рублю')
            # засыпаем на сутки
            await asyncio.sleep(3600 * 24)


async def worker2():
    """
    Воркер отправлющий в базу данных 
    """
    while True:
        print("Worker 2 is running")
        await asyncio.sleep(2)


# async def main():
#     # await asyncio.gather(worker1(), worker2())
#     await asyncio.create_task(worker1())


# if __name__ == '__main__':
#     try:
#         asyncio.run(main(), debug=True)
#     except KeyboardInterrupt:
#         logging.info('Выход по ctrl+break')
