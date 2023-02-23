import dataclasses
from typing import List


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def cost_of_road(self, shop_location: list, fuel_price: float) -> float:
        location_shop_x, location_shop_y = shop_location
        location_person_x, location_person_y = self.location
        distance = ((location_shop_x - location_person_x) ** 2
                    + (location_shop_y - location_person_y) ** 2) ** 0.5
        costing = self.car.fuel_consumption * (distance / 100) * fuel_price
        return costing


@dataclasses.dataclass
class Car:
    brand: str
    fuel_consumption: float


def creating_customers_classes(customers: List[dict]) -> List[Customer]:
    return [Customer(**customer) for customer in customers]
