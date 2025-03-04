import asyncio
import aiohttp
from aiogram import Bot
import os

BOT_TOKEN = os.getenv("BOT_TOKEN")
CHAT_ID = os.getenv("CHAT_ID")
URL = "https://it.tlscontact.com/by/msq/page.php?pid=news&l=ru"

bot = Bot(token=BOT_TOKEN)

async def send_news():
    while True:
        try:
            async with aiohttp.ClientSession() as session:
                async with session.get(URL) as response:
                    news = await response.text()  # Получаем HTML страницы с новостями

            await bot.send_message(CHAT_ID, news[:4000], disable_web_page_preview=True)
        except Exception as e:
            print(f"Ошибка при отправке уведомления: {e}")

        await asyncio.sleep(3600)  # Ожидание 1 час
