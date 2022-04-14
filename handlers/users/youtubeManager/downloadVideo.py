from utils.misc import YoutubeManager
from aiogram import types, filters, dispatcher
import keyboards as kb
from loader import dp

# Callback 'Download Video(YouTube) -> Download Videos' button
@dp.callback_query_handler(filters.Text(startswith='yt_downloadVideo'), state=None)
async def cbYtDownload(call: types.CallbackQuery):

    for title in YoutubeManager.urlManagerTools.getUrlList().keys():
        await call.message.answer('Download "{}" start!'.format(title))
        YoutubeManager.downloadVideos.downloadVideo(YoutubeManager.urlManagerTools.getUrlList()[title],
                                                    YoutubeManager.directoryManagerTools.getСurrentDir())
        await call.message.answer('Video "{}" successfully loaded!'.format(title))
    await call.answer()
