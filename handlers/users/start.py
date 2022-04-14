from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
import keyboards as kb

@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(text='Choose an action!',
                         reply_markup=kb.default.keyboard.createKeyboardCmdStart())
