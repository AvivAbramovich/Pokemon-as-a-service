import os
import json

import jsonschema


def test_schema():
    schema_path = os.path.join(os.path.dirname(os.path.dirname(__file__)),
                               'paas', 'pokemon_schema.json')
    with open(schema_path) as f:
        schema = json.load(f)

    with open(os.path.join(os.path.dirname(__file__), 'pokemons.json')) as f:
        tests = json.load(f)

    for pokemon in tests:
        jsonschema.validate(pokemon, schema)