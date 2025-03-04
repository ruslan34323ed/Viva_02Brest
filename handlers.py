from aiogram import Router, types, F
from news_parser import fetch_latest_news

router = Router()

@router.message(F.text == "/start")
async def cmd_start(message: types.Message):
    """Команда /start"""
    await message.answer("Привет! Я бот, который показывает последние новости TLS Contact. Используй /news для получения последних новостей.")

@router.message(F.text == "/news")
async def cmd_news(message: types.Message):
    """Команда /news — проверяет последнюю новость"""
    news = await fetch_latest_news()
    await message.answer(news, parse_mode="Markdown", disable_web_page_preview=False)
