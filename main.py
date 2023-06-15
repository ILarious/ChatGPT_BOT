from dotenv import load_dotenv, find_dotenv
import os

import openai

from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor


load_dotenv(find_dotenv())

bot = Bot(os.getenv('BOT_TOKEN_API'))
openai.api_key = os.getenv('OPENAI_API_KEY')

dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message) -> None:
    await message.answer(text='Этот бот для генерации ответов использует ChatGPT. Задай любой вопрос')
    await message.delete()

@dp.message_handler()
async def send_sms_chatGPT(message: types.Message) -> None:
    response = openai.Completion.create(
        model="text-davinci-003",
        prompt=message.text,
        temperature=0.9,
        max_tokens=1000,
        top_p=1,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
    )

    await message.answer(text=response['choices'][0]['text'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
