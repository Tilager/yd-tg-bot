from aiogram.dispatcher.filters.state import State, StatesGroup

class UrlManager(StatesGroup):
    waiting_for_url = State()

class DirectoryManager(StatesGroup):
    waiting_for_directory = State()