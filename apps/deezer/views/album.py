from django.shortcuts import render
from django.contrib import messages
from deezer.config import API_HEADERS
import requests
import json

def album(request, id_album):
    url = f"https://deezerdevs-deezer.p.rapidapi.com/album/{id_album}"
    response = requests.request("GET", url, headers=API_HEADERS)
    album = json.loads(response.text)
    context = {
        "album": album,
    }
    return render(request, "deezer/album.html", context)
