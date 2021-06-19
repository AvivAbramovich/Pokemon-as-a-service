import os
import json

import jsonschema


def test_schema():
    package_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'paas')
    schema_path = os.path.join(package_path, 'pokemon_schema.json')
    with open(schema_path) as f:
        schema = json.load(f)

    with open(os.path.join(package_path, 'assets', 'pokemons.json')) as f:
        tests = json.load(f)

    for pokemon in tests:
        jsonschema.validate(pokemon, schema)