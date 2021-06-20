import dataclasses
from typing import List, Optional

from elasticsearch import Elasticsearch

from paas.dal import IPokemonDAL
from paas.pokemon import Pokemon


class ESPokemonDAL(IPokemonDAL):
    def __init__(self,
                 es_client: Optional[Elasticsearch] = None,
                 index_name: str = 'pokemon'):
        self._es_client = es_client if es_client else client_from_env()
        self._index_name = index_name

    def create_pokemon(self, pokemon: Pokemon):
        # TODO: do pokemon have unique id? is nickname unique?
        self._es_client.index(self._index_name, body=pokemon.as_dict())

    def search(self, query: str) -> List[Pokemon]:
        body = {
            'query': {'query_string': {'query': f'{query}*'}}
        }
        results = self._es_client.search(index=self._index_name, body=body)
        hits = results['hits']['hits']
        return [Pokemon(**hit['_source']) for hit in hits]

    def health_check(self):
        if not self._es_client.ping():
            raise Exception('Database ping failed')


def client_from_env(
        host: Optional[str] = None,
        port: Optional[int] = None) -> Elasticsearch:
    import os
    if not host:
        host = os.getenv('ES_HOST', 'localhost')
    if not port:
        port = int(os.getenv('ES_PORT', 9200))

    return Elasticsearch([{'host': host, 'port': port}])
