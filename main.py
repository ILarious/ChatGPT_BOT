import openai
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

from config import BOT_TOKEN_API, OPENAI_API_KEY

bot = Bot(BOT_TOKEN_API)
openai.api_key = OPENAI_API_KEY

dp = Dispatcher(bot=bot)

@dp.message_handler(commands=['start'])
async def start_cmd(message: types.Message) -> None:
    await message.answer(text='это старт')
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

    print(f'Вопрос: {message.text}')
    print(f'Ответ: {response["choices"][0]["text"]}')

    await message.answer(text=response['choices'][0]['text'])


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
