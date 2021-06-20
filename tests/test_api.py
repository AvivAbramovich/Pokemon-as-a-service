import os
import json
import random
from typing import List, Dict, Set
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
    with open(os.path.join(os.path.dirname(__file__), 'autocomplete_tests.json')) as f:
        autocomplete_tests: List[Dict] = json.load(f)

    for ind, test in enumerate(autocomplete_tests, 1):
        query: str = test['query']
        expected_results: Set[int] = set(test['result_pokemons_id'])

        print(f'test {ind} - {query=} [expecting {len(expected_results)} result(s)]')
        res = requests.get(API_BASE + '/autocomplete/' + query, json=query)
        assert res.ok
        assert res.headers['content-type'] == 'application/json'
        results = res.json()

        results = set([d['pokadex_id'] for d in results])
        assert results == expected_results
