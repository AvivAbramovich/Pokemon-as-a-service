import os
import json

import pytest
import jsonschema


def test_schema():
    project_root_path = os.path.dirname(os.path.dirname((__file__)))
    schema_path = os.path.join(project_root_path, 'pokemon_schema.json')
    with open(schema_path) as f:
        schema = json.load(f)

    with open(os.path.join(project_root_path, 'assets', 'pokemons.json')) as f:
        tests = json.load(f)

    for pokemon in tests:
        jsonschema.validate(pokemon, schema)