import json
from typing import Dict, List

import jsonschema

from paas.pokemon import Pokemon
from paas.dal import IPokemonDAL


class NotValidPokemonError(Exception):
    def __init__(self, data: Dict):
        self.invalid_data = data

    def __str__(self):
        return f'The given dictionary is not a valid Pokemon: "{json.dumps(self.invalid_data)}"'


class PokemonBL:
    def __init__(self, pokemon_schema: Dict, dal: IPokemonDAL):
        self._schema = pokemon_schema
        self._dal = dal

    def health(self):
        self._dal.health_check()

    def index_pokemon(self, d: Dict):
        try:
            jsonschema.validate(d, self._schema)
        except jsonschema.exceptions.ValidationError:
            raise NotValidPokemonError(d)
        p = Pokemon(**d)
        self._dal.create_pokemon(p)

    def query(self, query: str) -> List[Pokemon]:
        return self._dal.search(query)
