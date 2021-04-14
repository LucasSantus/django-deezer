from django.contrib import admin
from django.urls import path
from deezer.views import index, album

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", index, name="index"),
    path("album/<int:id_album>", album, name="album"),
]