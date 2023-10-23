import dataclasses
from typing import List
from app.car import Car
from app.shop import Shop


@dataclasses
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int
    car: Car

    def ride_to_shop(self, trip_cost: float, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.money -= trip_cost
        self.location = shop.location



    
 