import os
import json
import random
from typing import List, Dict
import time

import requests
import pytest

API_BASE = os.getenv('PAAS_API_BASE', 'http://localhost:5000/api/')
NUM_TESTS = 100

with open(os.path.join(os.path.dirname(__file__), 'pokemons.json')) as f:
    test_pokemon: List[Dict] = json.load(f)


def get_random_str(main_str, substr_len):
    # Randomly select an "idx" such that "idx + substr_len <= len(main_str)".
    idx = random.randrange(0, len(main_str) - substr_len + 1)
    return main_str[idx: (idx+substr_len)]


def test_put_pokemon():
    for ind, pokemon in enumerate(test_pokemon, 1):
        print(f'test "put" #{ind} - "{pokemon["name"]}"')
        res = requests.post(API_BASE, json=pokemon)
        assert res.ok


@pytest.mark.dependency(depends=['test_put_pokemon'])
def test_search_pokemon():
    # sleep for 2 seconds because ES index takes some time to index new records
    time.sleep(2)
    for pokemon in test_pokemon:
        print(f'test search on pokemon "{pokemon["name"]}"')
        text_keys = list(filter(lambda key: type(pokemon[key]) is not int,
                                pokemon.keys()))
        for ind in range(NUM_TESTS):
            # choose random key
            key = random.choice(text_keys)
            value = pokemon[key]
            if key == 'skills':
                value = random.choice(value)
            query = get_random_str(value, random.randint(1, len(value)))
            print(f'test {ind + 1} - query="{query}" (key="{key}", value="{value}")')
            res = requests.get(API_BASE + '/autocomplete/' + query, json=pokemon)
            assert res.ok
            assert res.headers['content-type'] == 'application/json'
            results = res.json()
            assert len(results)
            assert any(map(lambda item: item == pokemon, results))

