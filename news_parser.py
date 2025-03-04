import aiohttp
from bs4 import BeautifulSoup
from config import URL

async def fetch_latest_news():
    """Получает последнюю новость с сайта"""
    async with aiohttp.ClientSession() as session:
        async with session.get(URL) as response:
            html = await response.text()

    soup = BeautifulSoup(html, "html.parser")
    news_section = soup.find("div", class_="news-content")  # Контейнер с новостями

    if not news_section:
        return "Новости не найдены."

    # Найти все элементы с новостями
    news_items = news_section.find_all(["h1", "h2", "p", "a"])

    if not news_items:
        return "Новости не найдены."

    # Берём первую новость
    latest_news = ""
    first_news = news_items[:5]  # Ограничиваем количество элементов

    base_url = "https://it.tlscontact.com"  # Добавляем базовый URL для ссылок
    for element in first_news:
        if element.name in ["h1", "h2"]:
            latest_news += f"📰 *{element.get_text()}*\n\n"
        elif element.name == "p":
            latest_news += f"{element.get_text()}\n\n"
        elif element.name == "a":
            link = element.get("href")
            full_link = f"{base_url}{link}" if link.startswith("/") else link
            latest_news += f"[🔗 Подробнее]({full_link})\n\n"

    return latest_news
