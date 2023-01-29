import requests
import pytest

def test_status_code():
    response = requests.get('https://pokemonbattle.me:5000/trainers?trainer_id=1937')
    assert response.status_code == 200
    