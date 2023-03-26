import asyncio
"""
Your user ID: 257804072
Current chat ID: 257804072
"""

import logging
from aiogram import Bot, Dispatcher, executor, types

import broadcast

from os import environ
from dotenv import load_dotenv
load_dotenv()

# Токен для управления ботом
API_TOKEN = environ['API_TOKEN']

# Включаем логирование, чтобы не пропустить важные сообщения
logging.basicConfig(level=logging.INFO)
log = logging.getLogger('bot_main')

# Объект бота
bot = Bot(token=API_TOKEN)

# Инициализация диспетчера бота
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    """
    Обработчик для команды /start ботa
    """
    logging.info("Запрошена команда /start")
    await message.reply(f"Ваш User ID: {message.from_user.id}\nТекущий Chat ID: {message.chat.id}")


@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
    """
    Обработчик для команды /help бота
    """
    logging.info("Запрошена команда /help")
    await message.reply("Пожалуйста, сообщите данные админинстратору")

# Запуск процесса поллинга новых апдейтов
async def main():
    await dp.start_polling()
    await broadcast.broadcaster()
    # executor.start_polling(dp, skip_updates=True)
    # executor.start(dp, broadcast.broadcaster())

if __name__ == '__main__':
    asyncio.run(main())