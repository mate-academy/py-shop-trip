from __future__ import annotations
from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float | int
