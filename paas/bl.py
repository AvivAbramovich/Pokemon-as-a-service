from typing import Dict, List

import jsonschema

from paas.pokemon import Pokemon
from paas.dal import IPokemonDAL


class PokemonBlError(Exception):
    pass


class PokemonBL:
    def __init__(self, pokemon_schema: Dict, dal: IPokemonDAL):
        self._schema = pokemon_schema
        self._dal = dal

    def index_pokemon(self, d: Dict) -> bool:
        try:
            jsonschema.validate(d, self._schema)
        except jsonschema.exceptions.ValidationError:
            raise PokemonBlError('The given dictionary is not a valid Pokemon')
        p = Pokemon(**d)
        index_res = self._dal.create_pokemon(p)
        # TODO: return true if index succeed
        raise NotImplementedError()

    def query(self, query: str) -> List[Pokemon]:
        raise NotImplementedError()
