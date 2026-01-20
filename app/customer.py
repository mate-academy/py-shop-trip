from dataclasses import dataclass


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int | float

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"
