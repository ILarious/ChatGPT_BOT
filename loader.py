from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

token = os.getenv('BOT_TOKEN_API')
openai_token = os.getenv('OPENAI_API_KEY')

bot = Bot(token=token, parse_mode=types.ParseMode.HTML)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)