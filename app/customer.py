import dataclasses
import datetime
from typing import Any


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float
    car: dict[str, [str, float]]

    @classmethod
    def load_from_dict(cls, customer: dict[str, Any]) -> None:
        cls.name = customer["name"]
        cls.product_cart = customer["product_cart"]
        cls.location = customer["location"]
        cls.money = customer["money"]
        cls.car = customer["car"]

    @staticmethod
    def the_cheapest_trip_to_the_store(shops: dict[str, float]) -> str:
        min_cost = min(shops.values())
        for shop_name, shop_value in shops.items():
            if shop_value == min_cost:
                return shop_name

    def print_check(
            self,
            cheapest_shop: dict[str, float],
            total_cost: float,
    ) -> None:
        date_purchase = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {date_purchase}")
        print(f"Thanks, {self.name}, for you purchase!\nYou have bought: ")
        for product in self.product_cart.keys():
            print(f"{self.product_cart[product]} {product}s "
                  f"for {cheapest_shop[product]} dollars")
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
