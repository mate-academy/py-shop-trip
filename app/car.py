from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    @classmethod
    def deserialize_from_dict(cls, info: dict) -> Car:
        return cls(info["brand"], info["fuel_consumption"])
