from django.shortcuts import render
from django.contrib import messages
import requests
import json

api_headers = {
    'x-rapidapi-key': "a9b2a659d9msh72c3634862390e2p1f856ejsn62022b3ffa9a",
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
}

def index(request):
    url = "https://deezerdevs-deezer.p.rapidapi.com/playlist/1111141961"
    
    list_musicas = requests.request("GET", url, headers=api_headers)

    if request.POST:
        url = "https://deezerdevs-deezer.p.rapidapi.com/search"
        pesquisa = request.POST.get("pesquisa", None)
        querystring = {"q": pesquisa}
        list_musicas = requests.request("GET", url, headers=api_headers, params=querystring)
    
    list_deezer = json.loads(list_musicas.text)
    
    print(f"\n\n\n\n{list_deezer}\n\n\n\n")

    if not list_deezer:
        messages.error(request, "Música não encontrada!")

    context = {
        "list": list_deezer,
    }

    return render(request, "deezer/index.html", context)

def album(request, id_album):

    url = f"https://deezerdevs-deezer.p.rapidapi.com/album/{id_album}"
    album = requests.request("GET", url, headers=api_headers)
    list_deezer = json.loads(album.text)
    context = {
        "list": list_deezer,
    }

    return render(request, "deezer/album.html", context)
