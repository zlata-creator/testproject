import json
import random
import os
from typing import List, Dict

# === НАСТРОЙКИ ===
DATA_FILE = "quotes_history.json"
QUOTES_FILE = "quotes_library.json"

# === ИНИЦИАЛИЗАЦИЯ БАЗОВОГО СПИСКА ЦИТАТ ===
def init_library() -> List[Dict[str, str]]:
    if os.path.exists(QUOTES_FILE):
        with open(QUOTES_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        quotes = [
            {"text": "Каждый человек — поэт, пока он не начинает писать стихи.", "author": "Иосиф Бродский", "topic": "творчество"},
            {"text": "Свобода — это ответственность.", "author": "Джордж Бернард Шоу", "topic": "философия"},
            {"text": "Наука — это организованные знания, мудрость — организованная жизнь.", "author": "Иммануил Кант", "topic": "знание"},
            {"text": "Смех — это звук мысли.", "author": "Алан Купер", "topic": "юмор"},
            {"text": "Будь собой. Все остальные роли уже заняты.", "author": "Оскар Уайльд", "topic": "личность"},
        ]
        save_library(quotes)
        return quotes

def save_library(quotes: List[Dict[str, str]]):
    with open(QUOTES_FILE, "w", encoding="utf-8") as f:
        json.dump(quotes, f, ensure_ascii=False, indent=4)

# === ИСТОРИЯ СГЕНЕРИРОВАННЫХ ЦИТАТ ===
def load_history() -> List[Dict[str, str]]:
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    return []

def save_history(history: List[Dict[str, str]]):
    with open(DATA_FILE, "w", encoding="utf-8") as f:
        json.dump(history, f, ensure_ascii=False, indent=4)

# === ОСНОВНЫЕ ФУНКЦИИ ===
def add_quote(library: List[Dict[str, str]]):
    print("\n--- Добавление новой цитаты ---")
    text = input("Текст цитаты: ").strip()
    if not text:
        print("❌ Ошибка: текст цитаты не может быть пустым.")
        return
    author = input("Автор: ").strip()
    if not author:
        print("❌ Ошибка: автор не может быть пустым.")
        return
    topic = input("Тема: ").strip()
    if not topic:
        print("❌ Ошибка: тема не может быть пустой.")
        return

    new_quote = {"text": text, "author": author, "topic": topic}
    library.append(new_quote)
    save_library(library)
    print("✅ Цитата добавлена!")

def generate_quote(library: List[Dict[str, str]], history: List[Dict[str, str]]):
    if not library:
        print("📚 Библиотека цитат пуста.")
        return
    quote = random.choice(library)
    history.append(quote)
    save_history(history)
    print("\n✨ Сгенерирована цитата:")
    print(f"“{quote['text']}”")
    print(f"— {quote['author']} ({quote['topic']})")

def show_history(history: List[Dict[str, str]]):
    if not history:
        print("📜 История пуста.")
        return
    print("\n--- История сгенерированных цитат ---")
    for i, quote in enumerate(history, 1):
        print(f"{i}. “{quote['text']}” — {quote['author']} ({quote['topic']})")

def filter_by_author(history: List[Dict[str, str]]):
    if not history:
        print("📜 История пуста.")
        return
    author_query = input("Введите имя автора: ").strip().lower()
    filtered = [q for q in history if author_query in q["author"].lower()]
    if not filtered:
        print("❌ Цитат этого автора не найдено.")
        return
    print(f"\n--- Цитаты автора: {author_query.title()} ---")
    for q in filtered:
        print(f"“{q['text']}” — {q['author']} ({q['topic']})")

def filter_by_topic(history: List[Dict[str, str]]):
    if not history:
        print("📜 История пуста.")
        return
    topic_query = input("Введите тему: ").strip().lower()
    filtered = [q for q in history if topic_query in q["topic"].lower()]
    if not filtered:
        print("❌ Цитат по этой теме не найдено.")
        return
    print(f"\n--- Цитаты по теме: {topic_query.title()} ---")
    for q in filtered:
        print(f"“{q['text']}” — {q['author']} ({q['topic']})")

# === МЕНЮ ===
def show_menu():
    print("\n" + "="*40)
    print("      Управление цитатами")
    print("="*40)
    print("1. Сгенерировать случайную цитату")
    print("2. Показать историю")
    print("3. Фильтровать по автору")
    print("4. Фильтровать по теме")
    print("5. Добавить новую цитату")
    print("6. Выйти")
    print("="*40)

# === ОСНОВНОЙ ЦИКЛ ===
def main():
    print("🚀 Добро пожаловать в приложение «Цитаты»!")
    library = init_library()
    history = load_history()

    while True:
        show_menu()
        choice = input("Выберите действие (1-6): ").strip()

        if choice == "1":
            generate_quote(library, history)
        elif choice == "2":
            show_history(history)
        elif choice == "3":
            filter_by_author(history)
        elif choice == "4":
            filter_by_topic(history)
        elif choice == "5":
            add_quote(library)
        elif choice == "6":
            print("👋 До новых встреч Мудрость всегда рядом.")
            break
        else:
            print("❌ Неверный выбор. Пожалуйста, введите число от 1 до 6.")
