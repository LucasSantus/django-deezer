from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json

def index(request):
    url = "https://deezerdevs-deezer.p.rapidapi.com/search"

    headers = {
        'x-rapidapi-key': "a9b2a659d9msh72c3634862390e2p1f856ejsn62022b3ffa9a",
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
    }

    context = None

    if request.POST:
        pesquisa = request.POST.get("pesquisa", None)
                   
        querystring = {"q": pesquisa}

        list_musicas = requests.request("GET", url, headers=headers, params=querystring)

        list_deezer = json.loads(list_musicas.text)

        print("PESQUISA DE MÚSICA\n\n\n")
        print(list_deezer)

        if not list_deezer:
            messages.error(request, "Música não encontrada!")

        context = {
            "list_deezer": list_deezer,
        }

    return render(request, "deezer/index.html", context)

def album(request, id_album):

    url = "https://deezerdevs-deezer.p.rapidapi.com/album/%7B1%7D"

    headers = {
        'x-rapidapi-key': "a9b2a659d9msh72c3634862390e2p1f856ejsn62022b3ffa9a",
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
    }

    album = requests.request("GET", url, headers=headers)

    list_deezer = json.loads(album.text)

    print("\n\n")
    print(list_deezer)
    print("\n\n")

    context = {
        "list_deezer": list_deezer,
    }

    return render(request, "deezer/album.html", context)
