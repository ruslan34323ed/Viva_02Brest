import sqlite3
from config import DB_NAME

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS last_news (
            id INTEGER PRIMARY KEY, 
            title TEXT
        )
    """)
    conn.commit()
    conn.close()

def get_last_saved_title():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT title FROM last_news ORDER BY id DESC LIMIT 1")
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None

def save_last_title(title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("DELETE FROM last_news")
    cursor.execute("INSERT INTO last_news (title) VALUES (?)", (title,))
    conn.commit()
    conn.close()
