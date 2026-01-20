from __future__ import annotations

from dataclasses import dataclass


@dataclass
class Product:
    name: str
    price: int | float
