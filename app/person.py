from dataclasses import dataclass
import datetime
from app.trip import Trip


@dataclass
class Person:
    name: str
    product_cart: dict
    location: list
    money: int | float
    fuel_consumption: int | float

    def trip(self, stores: dict, cheapest_store: Trip) -> None | str:
        print(f"{self.name} has {self.money} dollars")
        for price, store in stores.items():
            print(f"{self.name}'s trip to the {store.name} costs {price}")
        if self.money < min(stores.keys()):
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            return "stop"
        else:
            print(f"{self.name} rides to {cheapest_store.name}\n")
        self.location = cheapest_store.shop_location

    def check(self, cheapest_store: Trip, cheapest_trip: int | float) -> None:
        products_check = cheapest_store.money_for_products(self.product_cart)
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {self.name}, for your purchase!\n"
            f"You have bought: "
        )
        if self.product_cart["milk"]:
            print(f"{self.product_cart['milk']} "
                  f"milks for {products_check['milk']} dollars")
        if self.product_cart["bread"]:
            print(f"{self.product_cart['bread']} "
                  f"breads for {products_check['bread']} dollars")
        if self.product_cart["butter"]:
            print(f"{self.product_cart['butter']} "
                  f"butters for {products_check['butter']} dollars")
        print(
            f"Total cost is {sum(products_check.values())} dollars\n"
            f"See you again!\n"
        )
        self.money -= cheapest_trip

    def home(self) -> None:
        print(
            f"{self.name} rides home\n"
            f"{self.name} now has {self.money} dollars\n"
        )
