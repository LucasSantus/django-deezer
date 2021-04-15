from django.shortcuts import render, redirect
from django.contrib import messages
import requests
import json

def index(request):

    url = "https://deezerdevs-deezer.p.rapidapi.com/playlist/1111141961"

    headers = {
        'x-rapidapi-key': "a9b2a659d9msh72c3634862390e2p1f856ejsn62022b3ffa9a",
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
    }

    list_musicas = requests.request("GET", url, headers=headers)

    list_deezer = json.loads(list_musicas.text)

    print("TOP Musica\n\n\n")
    print(list_deezer)
   
    context = {
        "list": list_deezer,
    }

    if request.POST:

        url = "https://deezerdevs-deezer.p.rapidapi.com/search"

        pesquisa = request.POST.get("pesquisa", None)
                   
        querystring = {"q": pesquisa}

        list_musicas = requests.request("GET", url, headers=headers, params=querystring)

        list_deezer = json.loads(list_musicas.text)

        print("PESQUISA DE MÚSICA\n\n\n")
        print(list_deezer)

        if not list_deezer:
            messages.error(request, "Música não encontrada!")

        context = {
            "list": list_deezer,
        }

    return render(request, "deezer/index.html", context)

def album(request, id_album):

    url = "https://deezerdevs-deezer.p.rapidapi.com/album/{}".format(id_album)

    headers = {
        'x-rapidapi-key': "a9b2a659d9msh72c3634862390e2p1f856ejsn62022b3ffa9a",
        'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
    }
    album = requests.request("GET", url, headers=headers)
    
    list_deezer = json.loads(album.text)
    
    print("PESQUISA DE ALBUM")
    print(list_deezer)
    print("\n\n")

    context = {
        "list": list_deezer,
    }

    return render(request, "deezer/album.html", context)
