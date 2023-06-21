from aiogram import executor
from loader import dp

import handlers
from buttons.command_bot_sandwich import default_commands


async def on_startup(dispatcher):
    await default_commands(dispatcher)

if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup, skip_updates=True)
