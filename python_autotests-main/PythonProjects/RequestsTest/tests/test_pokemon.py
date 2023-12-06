import requests
import pytest

token = '3035fed27f31ff3786be11d75323f31c'
host = 'https://api.pokemonbattle.me:9104'

def test_status_cod():
    response = requests.get(f'{host}/trainers')
    assert response.status_code == 200

def test_part_of_answer():
    response = requests.get(f'{host}/trainers', params = {'trainer_id' : 1858})
    assert response.json()['trainer_name'] == 'Davidson'