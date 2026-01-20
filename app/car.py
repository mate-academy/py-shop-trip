from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @classmethod
    def from_dict(cls, dict_: dict) -> Car:
        return cls(**dict_)
