import dataclasses
from typing import List


@dataclasses.dataclass
class Pokemon:
    pokadex_id: int
    name: str
    nickname: str
    level: int
    type: str
    skills: List[str]
