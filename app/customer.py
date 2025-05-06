import math
import datetime
from decimal import Decimal
from dataclasses import dataclass

from app.car import Car
from app.product import Product
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: Product
    location: list
    money: float
    car: Car

    @classmethod
    def from_dict(cls, params: dict) -> "Customer":
        return cls(
            name=params["name"],
            product_cart=Product(**params["product_cart"]),
            location=params["location"],
            money=params["money"],
            car=Car(**params["car"])
        )

    def distance_to_shop(self, shop: Shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return round(math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2), 3)

    def groceries_cost(self, other: Shop) -> float:
        return (
            self.product_cart.milk * other.products.milk
            + self.product_cart.bread * other.products.bread
            + self.product_cart.butter * other.products.butter
        )

    def have_enough_money(self, price: float) -> bool:
        return self.money >= price

    def pay_for_trip_and_groceries(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        distance = self.distance_to_shop(shop)
        pay_for_trip = self.car.trip_cost(distance, fuel_price)
        return round(self.groceries_cost(shop) + 2 * pay_for_trip, 2)

    def pay_for_groceries(self, price: float) -> None:
        self.money -= price
        print(f"{self.name} now has {self.money} dollars")
        print("")

    def print_check(self, other: Shop) -> None:
        date_now = datetime.datetime.now()
        print("")
        print(f"Date: {date_now.strftime("%d/%m/%Y %H:%M:%S")}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        print(f"{self.product_cart.milk} milks "
              f"for {Decimal(self.product_cart.milk * other.products.milk)}"
              f" dollars")
        print(f"{self.product_cart.bread} breads for "
              f"{Decimal(self.product_cart.bread * other.products.bread)} "
              f"dollars")
        print(f"{self.product_cart.butter} butters for "
              f"{self.product_cart.butter * other.products.butter} "
              f"dollars")
        print(f"Total cost is {self.groceries_cost(other)} dollars")
        print("See you again!")
        print("")
