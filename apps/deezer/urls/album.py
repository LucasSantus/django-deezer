from django.urls import path
from deezer.views import album

urlpatterns = [
    # ALBUM
    path("album/<int:id_album>/", album, name="album"),
]