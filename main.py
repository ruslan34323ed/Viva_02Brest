import asyncio
import aiohttp
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
from aiogram.filters import Command
from config import TOKEN, CHAT_ID, URL

bot = Bot(token=TOKEN)
dp = Dispatcher()
LAST_NEWS = None

async def fetch_news():
    global LAST_NEWS
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            
            news_blocks = soup.find_all('div', class_='d-flex py-4 align-items-start align-items-md-baseline mt-4')
            if news_blocks:
                latest_block = news_blocks[0]
                news_title = latest_block.find('h3').get_text(strip=True)
                
                # Получаем текст между новым H3 и предыдущим H3
                news_content = []
                for sibling in latest_block.find_next_siblings():
                    if sibling.find('h3'):
                        break  # Остановиться на следующем заголовке
                    news_content.append(sibling.get_text(strip=True))
                
                full_news = (
                    f"📢 <b>{news_title}</b>\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                    + '\n'.join([f"🔹 {line}" for line in news_content]) + "\n"
                    f"━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\n"
                    f"🔗 <a href='{URL}'>Подробнее на сайте</a>"
                )
                
                if full_news != LAST_NEWS:
                    LAST_NEWS = full_news
                    await bot.send_message(CHAT_ID, f"🔔 <b>Новая новость:</b> \n\n{full_news}", parse_mode="HTML")

async def check_updates():
    while True:
        await fetch_news()
        await asyncio.sleep(3600)  # Проверяем страницу раз в час

@dp.message(Command("start"))
async def start_command(message: Message):
    await message.answer("Привет! Я бот для уведомлений о новых новостях. /news")

@dp.message(Command("latest"))
async def latest_news(message: Message):
    if LAST_NEWS:
        await message.answer(f"<b>Последняя новость:</b> \n\n{LAST_NEWS}", parse_mode="HTML")
    else:
        await message.answer("Пока нет новостей.")

async def main():
    asyncio.create_task(check_updates())
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
