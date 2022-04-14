from pytube import YouTube

def downloadVideo(idVideo: str, path: str = None):
    url = 'https://www.youtube.com/watch?v={}'.format(idVideo)
    video = YouTube(url)
    video.streams.filter(progressive=True).last().download(output_path=path)
    return