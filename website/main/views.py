import pafy
from django.shortcuts import render
from django.template.defaultfilters import filesizeformat

from .forms import UrlForm


def get_url(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            video = pafy.new(form.cleaned_data["url"])
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
            context = {
                "form": form,
                "streams": video_streams
            }
            return render(request, "main.html", context)
    else:
        form = UrlForm()
    return render(request, "main.html", {"form": form})
