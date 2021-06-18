from typing import List, Optional

from elasticsearch import Elasticsearch

from paas.dal import IPokemonDAL
from paas.pokemon import Pokemon


class ESPokemonDAL(IPokemonDAL):
    def __init__(self,
                 es_client: Optional[Elasticsearch] = None,
                 index_name: str = 'Pokemon'):
        self._es_client = es_client if es_client else client_from_env()
        self._index_name = index_name

    def create_pokemon(self, pokemon: Pokemon):
        self._es_client.index(self._index_name, body=pokemon)

    def autocomplete(self, query: str) -> List[Pokemon]:
        raise NotImplementedError()


def client_from_env(
        host: Optional[str] = None,
        port: Optional[int] = None) -> Elasticsearch:
    import os
    if not host:
        host = os.getenv('ES_HOST', 'localhost')
    if not port:
        port = int(os.getenv('ES_PORT', 9200))

    return Elasticsearch([{'host': host, 'port': port}])
