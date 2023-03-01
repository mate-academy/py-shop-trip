from dataclasses import dataclass

FUEL_PRICE = 2.4


@dataclass
class Car:
    _brand: str
    _fuel_consumption: float

    @property
    def fuel_consumption_in_km(self) -> float:
        return self._fuel_consumption / 100
