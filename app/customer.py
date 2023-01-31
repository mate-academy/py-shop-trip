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
    def cheapest_trip(shops: dict[str, float]) -> str:
        lowest_prices = min(shops.values())
        for shop_name, shop_prices in shops.items():
            if shop_prices == lowest_prices:
                return shop_name

    def info_output(
            self,
            cheapest_shop: dict[str, float],
            total_price: float
    ) -> None:
        modified_today = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {modified_today}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        for product in self.product_cart.keys():
            print (f"{self.product_cart[product]} {product}s "
                   f"for {cheapest_shop[product]} dollars")
        print(f"Total cost is {total_price} dollars")
        print("See you again!\n")
