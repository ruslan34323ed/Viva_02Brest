import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

TOKEN = os.getenv("BOT_TOKEN")  # Получаем токен бота из .env
CHAT_ID = os.getenv("CHAT_ID")  # Получаем ID чата из .env
URL = "https://it.tlscontact.com/by/bqt/page.php?pid=news&l=ru"  # URL страницы с новостями
DB_NAME = "news.db"
CHECK_INTERVAL = 3600  # Проверка новостей раз в час

# Проверяем, что переменные загружены корректно
if not TOKEN:
    raise ValueError("Ошибка: BOT_TOKEN не найден в переменных окружения!")
if not CHAT_ID:
    raise ValueError("Ошибка: CHAT_ID не найден в переменных окружения!")
