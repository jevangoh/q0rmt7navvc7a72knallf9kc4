from __future__ import annotations
from typing import Optional

from uuid import UUID as Uuid

import kac6tplvgexvn24jij4v7bhsc as Enumerator


class q0rmt7navvc7a72knallf9kc4(Enumerator._):
    def __init__(self, level: int, string: str, id: Optional[Uuid] = None):
        self.level: int = level
        self.string: str = string
        super().__init__(level, string, id=id)

    def to_level(self) -> int:
        return self.level

    def to_string(self) -> str:
        return self.string
