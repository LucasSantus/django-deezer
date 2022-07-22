from django.shortcuts import render
from django.contrib import messages
import requests
import json

def album(request, id_album):
    url = f"https://deezerdevs-deezer.p.rapidapi.com/album/{id_album}"
    album = requests.request("GET", url, headers=api_headers)
    list_deezer = json.loads(album.text)
    context = {
        "list": list_deezer,
    }
    return render(request, "deezer/album.html", context)
