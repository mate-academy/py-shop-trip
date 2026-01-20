import math
from typing import Any

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 products: dict,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def create_customer(customer_info: dict) -> Any:
        return Customer(
            name=customer_info["name"],
            products=customer_info["product_cart"],
            location=customer_info["location"],
            money=customer_info["money"],
            car=Car(brand=customer_info["car"]["brand"],
                    fuel_consumption=customer_info["car"]["fuel_consumption"])
        )

    def get_trip_cost(self,
                      fuel_price: float,
                      shop: Shop) -> float:
        fuel_cost = self._get_dist_to_shop(shop.location) * \
                    self.car.fuel_consumption * \
                    fuel_price / 50
        return round(fuel_cost + shop.get_total_cost(self.products), 2)

    def _get_dist_to_shop(self,
                          shop_location: list,
                          ) -> float:
        ax = self.location[0]
        ay = self.location[1]
        bx = shop_location[0]
        by = shop_location[1]

        distance = math.sqrt((bx - ax) ** 2 + (by - ay) ** 2)

        return distance
