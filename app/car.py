from app.shop import Shop
from app.customer import Customer

class Car:
    def __init__(self, brand: str, fuel_consumption: float, owner: Customer) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.owner = owner

    def to_shop(self, shop: Shop) -> None:
        print(f"{self.owner.name} rides to {shop.name}")
