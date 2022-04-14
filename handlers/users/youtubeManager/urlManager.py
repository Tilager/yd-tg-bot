from aiogram import types, filters, dispatcher
from loader import dp
import keyboards as kb
from states.youtubeManagerStates import UrlManager
from data.dataBases import urlList
from utils.misc.YoutubeManager import urlManagerTools


# Button Download Video(YouTube)
@dp.message_handler(filters.Text(equals='Download video(YouTube)'), state=None)
async def downloadVideo(message: types.Message):
    await message.answer(text='Video Download Manager',
                         reply_markup=kb.inline.keyboard.createKeyboardYoutubeManager())

# Callback 'Download Video(YouTube) -> Url Manager' button
@dp.callback_query_handler(filters.Text(startswith='yt_urlManager'), state=None)
async def cbYtUrl(call: types.CallbackQuery):
    await call.message.answer('Videos list: [\n{},]'.format('\n'.join(urlList.keys())),
                              disable_web_page_preview=True,
                              reply_markup=kb.inline.keyboard.createKeyboardUrlManager())
    await call.answer()

# Callback 'Download Video(YouTube) -> Url Manager -> Add/Accept' buttons
@dp.callback_query_handler(filters.Text(startswith='yt_um_'))
async def cbYtUrlManager(call: types.CallbackQuery):
    action = call.data.split('_')[2]
    match action:
        case 'add':
            # 'Download Video(YouTube) -> 'Url Manager -> Add' button
            await call.message.reply('Enter URL:')
            await call.answer()
            await UrlManager.waiting_for_url.set()
        case 'accept':
            # 'Download Video(YouTube) -> 'Url Manager -> Accept' button
            await call.answer()
            await call.message.answer(text='Video Download Manager',
                     reply_markup=kb.inline.keyboard.createKeyboardYoutubeManager())

    await call.answer()

# Dispatcher 'Url Manager -> Add' state
@dp.message_handler(state=UrlManager.waiting_for_url)
async def addUrlList(msg: types.Message, state: dispatcher.FSMContext):
    match urlManagerTools.addUrl(msg.text):
        case -1: # Incorrect link error
            await msg.answer('Incorrect link entered!')
            print('User ({}) entered incorrect link!'.format(msg.from_user.id))
        case 1: # The link is repeated
            await msg.answer("This video has already been!")
    await msg.answer('Videos list - [{}, ]'.format('\n'.join(urlList.keys())),
                     disable_web_page_preview=True,
                     reply_markup=kb.inline.keyboard.createKeyboardUrlManager())
    await state.finish()