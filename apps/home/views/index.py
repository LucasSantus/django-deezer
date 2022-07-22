from django.shortcuts import render
from django.contrib import messages
from deezer.config import API_HEADERS
from home.default_messages import DEFAULT_MESSAGES
import requests
import json

def index(request):
    url = "https://deezerdevs-deezer.p.rapidapi.com/playlist/1111141961"
    response = requests.request("GET", url, headers=API_HEADERS)

    if request.POST:
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"
        search = request.POST.get("search", "Yummy")
        query = {"q": search}
        response = requests.request("GET", url, headers=API_HEADERS, params=query)

    musics = json.loads(response.text)

    if not musics:
        messages.error(request, DEFAULT_MESSAGES['MUSIC_NOT_FOUND'])

    print("\n\n\n\n\n\n\n\n\n\n\n")
    print(musics)
    print("\n\n\n\n\n\n\n\n\n\n\n")
    
    context = {
        "musics": musics,
    }

    return render(request, "home/index.html", context)

