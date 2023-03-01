from dataclasses import dataclass


@dataclass
class Product:
    _name: str
    _price: float

    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price
