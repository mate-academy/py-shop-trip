from __future__ import annotations

from dataclasses import dataclass
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.shop import Shop


@dataclass()
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: dict

    @classmethod
    def from_dict(cls, data: dict) -> Customer:
        return cls(
            **{
                key: data[key]
                for key in cls.__annotations__ if key in data
            }
        )

    def choice_shop(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> tuple[Shop, float]:
        self.home_location = self.location
        price_shop = {}

        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            price = sum(
                self.product_cart[product]
                * shop.products.get(product, 0)
                for product in self.product_cart
            )

            price += ((self.car["fuel_consumption"] / 100) * fuel_price
                      * self.calculate_distance(shop.location) * 2)
            price = round(price, 2)

            print(f"{self.name}\'s trip to the {shop.name} costs {price}")

            price_shop[price] = shop

        cheapest_price = min(price_shop)
        return price_shop[cheapest_price], cheapest_price

    def calculate_distance(self, new_location: list) -> float:
        distance = ((self.location[0] - new_location[0]) ** 2
                    + (self.location[1] - new_location[1]) ** 2) ** 0.5

        return distance

    def come_back_home(self, cost_of_the_trip: float) -> None:
        print(f"{self.name} rides home")

        self.location = self.home_location
        self.home_location = None
        self.money -= cost_of_the_trip

        print(f"{self.name} now has {self.money} dollars\n")
