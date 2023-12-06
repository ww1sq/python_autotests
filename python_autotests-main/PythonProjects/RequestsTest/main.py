import requests

token = '3035fed27f31ff3786be11d75323f31c'
host = 'https://api.pokemonbattle.me:9104'

'''response_add_pokemon = requests.post(f'{host}/pokemons', json = {
    "name": "Таити",
    "photo": "https://dolnikov.ru/pokemons/albums/001.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print(response_add_pokemon.text)'''

'''response_update_pokemon = requests.put(f'{host}/pokemons', json = {
    "pokemon_id": "5578",
    "name": "Гавайи",
    "photo": "https://dolnikov.ru/pokemons/albums/008.png"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print(response_update_pokemon.text)'''

'''response_add_pokeball = requests.post(f'{host}/trainers/add_pokeball', json = {
    "pokemon_id": "5578"
}, headers = {'Content-Type' : 'application/json',
              'trainer_token' : token})

print(response_add_pokeball.text)'''