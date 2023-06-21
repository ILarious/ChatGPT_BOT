from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp, bot
from handlers.keyboards import get_kb_start
from urls.urls import PREVIEW_PHOTO

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    TEXT = f"Привет, {message.from_user.full_name}!\n" \
           f"Этот бот предоставит доступ к ChatGPT."
    await bot.send_photo(chat_id=message.chat.id,
                         caption=TEXT,
                         photo=PREVIEW_PHOTO,
                         reply_markup=get_kb_start())