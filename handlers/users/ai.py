from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Text

from loader import dp, bot
from buttons.keyboards import get_kb_chat, get_kb_start
from states.talk_state import AI
import openai


@dp.callback_query_handler(text='start')
async def chat_start(call: types.CallbackQuery, state: FSMContext):
    await call.message.answer(
        text="Отправь сообщение, чтобы начать переписку",
        reply_markup=get_kb_chat()
    )
    await AI.talk.set()
    await state.update_data(history=[{"question": None, "answer": None}])


@dp.message_handler(Text(equals='закончить чат', ignore_case=True), state='*')
async def back(message: types.Message, state: FSMContext):
    TEXT = f"Всего доброго, {message.from_user.full_name}!\n" \
           f"Возвращайтесь снова!"

    await message.answer(
        text=TEXT,
        reply_markup=get_kb_start()
    )
    await state.finish()


@dp.message_handler(Text(equals='стереть память', ignore_case=True), state='*')
async def clear(message: types.Message, state: FSMContext):
    await message.answer('Память ИИ стерта')
    await state.update_data(history=[{"question": None, "answer": None}])


@dp.message_handler(state=AI.talk)
async def chat_talk(message: types.Message, state: FSMContext):
    data = await state.get_data()
    data = data.get('history')

    msg = await message.answer("ИИ думает...")

    history = []
    if len(data) > 1:
        for index in range(0, len(data)):
            if data[index].get('question') is None:
                data[index]['question'] = message.text
                d = {"role": "user", "content": data[index]['question']}
                history.append(d)
            else:
                d = [
                    {"role": "user", "content": data[index]['question']},
                    {"role": "assistant", "content": data[index].get('answer')}
                ]
                history += d
    else:
        data[0]['question'] = message.text
        d = {"role": "user", "content": data[0].get('question')}
        history.append(d)

    print(history)

    request = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=history,
        max_tokens=500,
        temperature=1,
    )

    resp_ai = request['choices'][0]['message']['content']

    data[-1]['answer'] = resp_ai.replace('\n', '')
    data.append({"question": None, "answer": None})

    if len(data) > 10:
        await state.update_data(history=[{"question": None, "answer": None}])
    await state.update_data(history=data)

    await msg.delete()
    await message.answer(resp_ai)
