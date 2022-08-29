import pafy
from django.shortcuts import render
from django.template.defaultfilters import filesizeformat
from .forms import UrlForm
from .logic import return_video


def page_not_found_view(request):
    return render(request, '404.html', status=404)


def get_video(request):
    if request.method == "POST":
        form = UrlForm(request.POST)
        if form.is_valid():
            try:
                context = {
                    "form": form,
                    "streams": return_video(form.cleaned_data["url"])
                }
                return render(request, "main.html", context)
            except Exception:
                return render(request, "404.html")
    else:
        form = UrlForm()
    return render(request, "main.html", {"form": form})
