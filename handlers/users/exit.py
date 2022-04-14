from aiogram.dispatcher.filters import Command
from aiogram.types import Message

from data.config import ADMINS
from loader import dp, loop


@dp.message_handler(Command('exit'))
async def exitHandel(msg: Message):
    if str(msg.from_user.id) in ADMINS:
        await msg.answer('Bot stopping!')
        dp.stop_polling()
        await dp.wait_closed()
        loop.stop()
    else:
        await msg.answer("You don't have the necessary permissions.")
