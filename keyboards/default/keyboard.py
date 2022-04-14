from aiogram import types

# клавиатура при команде старт
def createKeyboardCmdStart():
    keyboardCmdStart = types.ReplyKeyboardMarkup(resize_keyboard=True,
                                            one_time_keyboard=True)
    buttons = [types.KeyboardButton(text='Download video(YouTube)', )]
    keyboardCmdStart.add(*buttons)
    return keyboardCmdStart

