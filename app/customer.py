import dataclasses


from app.car import Car


@dataclasses.dataclass()
class Customer:
    name: str
    product_cart: dict[str: int]
    location: list
    money: int
    car: Car
