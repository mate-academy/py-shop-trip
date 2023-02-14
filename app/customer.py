from __future__ import annotations
from typing import List

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[list],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def load_from_dict(cls, customer: dict) -> Customer:
        return cls(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]),
        )

    def calculate_way_to_shop(self, shop: Shop, fuel_prise: float) -> float:
        way_km = (
            ((self.location[0] - shop.location[0]) ** 2)
            + ((self.location[1] - shop.location[1]) ** 2)
        ) ** 0.5
        fuel_volume = way_km * self.car.fuel_consumption_for_100_km / 100
        return fuel_volume * fuel_prise

    def calculate_products_cost(self, shop: Shop) -> float:
        return sum(
            shop.products[product] * self.product_cart[product]
            for product, cost in self.product_cart.items()
        )

    def create_chek(self, shop: Shop) -> None:
        print("\nDate: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for you purchase!\nYou have bought: ")
        check_money = 0
        for product, count in self.product_cart.items():
            money = shop.products[product] * self.product_cart[product]
            check_money += money
            print(f"{count} {product}s for {money} dollars")
        print(f"Total cost is {check_money} dollars\nSee you again!\n")
