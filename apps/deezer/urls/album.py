from django.urls import path
from deezer.views import album

urlpatterns = [
    # INDEX
    path("", album, name="album"),
]