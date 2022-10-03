import dataclasses


@dataclasses.dataclass
class Customer:
    name: str
    products: dict
    location: list
    money: float
    fuel_consumption: float
