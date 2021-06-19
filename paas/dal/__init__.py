from abc import ABC, abstractmethod
from typing import List

from paas.pokemon import Pokemon


class IPokemonDAL(ABC):
    @abstractmethod
    def create_pokemon(self, pokemon: Pokemon):
        pass

    @abstractmethod
    def search(self, query: str) -> List[Pokemon]:
        pass

    def health_check(self):
        pass
