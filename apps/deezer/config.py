import os

KEY = str(os.environ.get('KEY', 'a9b2a659d9msh72c3634862390e2p1f856ejsn62022b3ffa9a'))

API_HEADERS = {
    'x-rapidapi-key': KEY,
    'x-rapidapi-host': "deezerdevs-deezer.p.rapidapi.com"
}