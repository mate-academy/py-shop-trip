import dataclasses


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict
