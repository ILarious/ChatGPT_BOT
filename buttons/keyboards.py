from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, \
    ReplyKeyboardMarkup, KeyboardButton


def get_kb_start() -> InlineKeyboardMarkup:
    kb = InlineKeyboardMarkup(row_width=1)
    start = InlineKeyboardButton(text="Начать чат с ИИ", callback_data="start")
    kb.add(start)

    return kb


def get_kb_chat() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    stop = KeyboardButton(text="Закончить чат")
    clear = KeyboardButton(text="Стереть память")
    kb.add(stop, clear)

    return kb
