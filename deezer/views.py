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

        print(list_deezer)

        if not list_deezer:
            messages.error(request, "Música não encontrada!")

        context = {
            "list_deezer": list_deezer,
        }

    return render(request, "deezer/index.html", context)

    # api_request = requests.get("http://127.0.0.1:8000/api/list/?search=")
    # list_musicas = json.loads(api_request.text)
    
    # if request.POST:
    #     pesquisa = request.POST.get("pesquisa", None)
                            
    #     api_request = None
    #     list_musicas = None

    #     api_request = requests.get("http://127.0.0.1:8000/api/list/?search="+pesquisa)
    #     list_musicas = json.loads(api_request.text)

    #     if not list_musicas: 
    #         api_request = requests.get("http://127.0.0.1:8000/api/music/?format=json")
    #         list_musicas = json.loads(api_request.text)

    #         messages.error(request, "Música não encontrada!")

    # context = {
    #     "list_musicas": list_musicas,
    # }
    # return render(request, "musica/index.html", context)