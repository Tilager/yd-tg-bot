from aiogram import types, filters, dispatcher
from loader import dp
import keyboards as kb
from states.youtubeManagerStates import DirectoryManager
from utils.misc.YoutubeManager import directoryManagerTools as dmt


# Callback 'Download Video(YouTube) -> Directory Manager' button
@dp.callback_query_handler(filters.Text(startswith='yt_directoryManager'), state=None)
async def cbYtUrl(call: types.CallbackQuery):
    await call.message.answer('Current directory: {}'.format(dmt.getСurrentDir()),
                              disable_web_page_preview=True,
                              reply_markup=kb.inline.keyboard.createKeyboardDirectoryManager())
    await call.answer()

@dp.callback_query_handler(filters.Text(startswith='yt_dm_'))
async def cbYtDirectoryManager(call: types.CallbackQuery):
    action = call.data.split('_')[2]
    match action:
        case 'edit':
            await call.message.reply('Enter Directory:')
            await DirectoryManager.waiting_for_directory.set()
        case 'accept':
            await call.message.answer(text='Video Download Manager',
                                      reply_markup=kb.inline.keyboard.createKeyboardYoutubeManager())
    await call.answer()

@dp.message_handler(state=DirectoryManager.waiting_for_directory)
async def editUrl(msg: types.Message, state: dispatcher.FSMContext):
    match dmt.editCurrentDir(msg.text):
        case -1:
            await msg.answer('Incorrect Directory!')
            print('User ({}) entered incorrect directory!'.format(msg.from_user.id))
    await msg.answer('Current directory: {}'.format(dmt.getСurrentDir()),
                     disable_web_page_preview=True,
                     reply_markup=kb.inline.keyboard.createKeyboardDirectoryManager())
    await state.finish()