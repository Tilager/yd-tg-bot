from pytube import YouTube, exceptions
from data.dataBases import urlList

def getUrlList():
    return urlList

def addUrl(url: str): # add Url in urlList
    try:
        video = YouTube(url=url)
    except exceptions.RegexMatchError:
        # incorrect link error
        return -1
    idVideo = url[url.find('=') + 1:None if url.find('&') == -1 else url.find('&')]
    if urlList.get(video.title, 0) == 0:
        urlList[video.title] = idVideo
    elif urlList.get(video.title, 0) != 0 and urlList[video.title] == idVideo:
        return 1
    else:
        # If the same title
        for x in range(1, 1000):
            if urlList.get('{} ({})'.format(video.title, x), 0) == 0:
                urlList['{} ({})'.format(video.title, x)] = idVideo
                break
            else:
                if (urlList['{} ({})'.format(video.title, x)] == idVideo):
                    break