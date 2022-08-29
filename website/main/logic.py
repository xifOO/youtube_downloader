import pafy
from django.template.defaultfilters import filesizeformat


def return_video(url):
    video = pafy.new(url)
    stream = video.streams
    video_streams = []
    for s in stream:
        video_streams.append({
            "resolution": s.resolution,
            "video_url": s.url + "&title=" + video.title,
            "extension": s.extension,
            "size": filesizeformat(s.get_filesize()),
            "title": video.title
        })
    return video_streams