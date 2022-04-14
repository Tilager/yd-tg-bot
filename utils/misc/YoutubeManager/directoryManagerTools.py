from os import getcwd, path
from data.dataBases import directoryYoutubeManager

def getСurrentDir():
    return getcwd() if not directoryYoutubeManager else directoryYoutubeManager

def editCurrentDir(dir: str):
    if path.exists(dir):
        global directoryYoutubeManager
        directoryYoutubeManager = dir
    else:
        return -1 # Incorrect Directory