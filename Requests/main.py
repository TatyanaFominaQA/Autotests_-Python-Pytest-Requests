import requests
import json

token = 'd85af345d24614fa6be48b06f9b9721c'

response = requests.post('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token},json={
    "name": "Бульбозавра Бульбозавр",
    "photo": "https://dolnikov.ru/pokemons/albums/10.png"
})

response = requests.put('https://pokemonbattle.me:5000/pokemons', headers={'trainer_token': token},json={
    "pokemon_id": 3813,
    "name": "Слоупок",
    "photo": ""
})

response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', headers={'trainer_token': token},json={
    "pokemon_id": "3813"

})

print(response.text)