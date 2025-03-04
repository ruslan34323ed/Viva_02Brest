from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
import asyncio
import logging
from config import BOT_TOKEN

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создаем бота с указанием формата сообщений по умолчанию
bot = Bot(token=BOT_TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.MARKDOWN))
dp = Dispatcher()


from aiogram import Bot
import asyncio
from config import CHAT_ID
from news_parser import fetch_latest_news
from bot import bot  # Импортируем бота

async def send_latest_news():
    """Отправляет последнюю новость в Телеграм"""
    news = await fetch_latest_news()
    await bot.send_message(CHAT_ID, news, disable_web_page_preview=False)

async def main():
    await send_latest_news()

if __name__ == "__main__":
    asyncio.run(main())
