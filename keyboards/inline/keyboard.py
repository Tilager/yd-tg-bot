from aiogram import types

# создание YouTube manager клавиатуры
def createKeyboardYoutubeManager():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text='Url Manager', callback_data='yt_urlManager'),
               types.InlineKeyboardButton(text='Directory Manager', callback_data='yt_directoryManager'),
               types.InlineKeyboardButton(text='Download Video', callback_data='yt_downloadVideo')]
    keyboard.add(*buttons)
    return keyboard

def createKeyboardUrlManager():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text='Add', callback_data='yt_um_add'),
               types.InlineKeyboardButton(text='Accept', callback_data='yt_um_accept')]
    keyboard.add(*buttons)
    return keyboard

def createKeyboardDirectoryManager():
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    buttons = [types.InlineKeyboardButton(text='Edit', callback_data='yt_dm_edit'),
               types.InlineKeyboardButton(text='Accept', callback_data='yt_dm_accept')]
    keyboard.add(*buttons)
    return keyboard