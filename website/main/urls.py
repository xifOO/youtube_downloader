from django.urls import path
from .views import get_url

urlpatterns = [
    path("", get_url, name="get_url"),
]