from datetime import datetime
from dataclasses import dataclass
from math import dist

from app.car import Car
from app.car import FUEL_PRICE
from app.shop import Shop


DATE_TIME = (datetime(2021, 1, 4, 12, 33, 41)
             .strftime("%d/%m/%Y %H:%M:%S"))


@dataclass
class Customer:
    _all_customers = []
    _name: str
    _products: dict[str: int]
    _location: list[int, int]
    _money: float
    _car: Car

    @classmethod
    def get_customers(cls) -> list["Customer"]:
        return cls._all_customers

    @property
    def name(self) -> str:
        return self._name

    @property
    def money(self) -> float:
        return self._money

    @money.setter
    def money(self, new_value: float) -> None:
        self._money = new_value

    @classmethod
    def create_customers_from_json(cls, json_data: dict) -> None:
        for customer in json_data["customers"]:
            name = customer["name"]
            location = customer["location"]
            money = customer["money"]
            car = Car(*customer["car"].values())
            list_of_products = {name: count
                                for name, count in
                                customer["product_cart"].items()}

            cls._all_customers.append(
                Customer(
                    name,
                    list_of_products,
                    location,
                    money,
                    car
                )
            )

    def cost_products_in_shop(self, shop: Shop) -> float:
        total_price = 0
        for name, count in self._products.items():
            total_price += shop.products[name].price * count
        return round(total_price, 2)

    def cost_drive(self, shop: Shop) -> float:
        distance_in_km = dist(self._location, shop.location)
        cost = (distance_in_km
                * 2 * self._car.fuel_consumption_in_km * FUEL_PRICE)
        return round(cost, 2)

    def _buy_products(self, shop: Shop) -> None:

        print(f"Date: {DATE_TIME}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        total_price = self.cost_products_in_shop(shop)

        self.cost_products_in_shop(shop)
        for name, count in self._products.items():
            print(f"{count} {name}s for "
                  f"{shop.products[name].price * count} dollars")

        print(f"Total cost is {total_price} dollars")
        print("See you again!\n")

    def _ride_shop(self, shop: Shop) -> None:
        self._location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def _ride_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def start_trip(self, shop: Shop) -> None:
        self._ride_shop(shop)
        self._buy_products(shop)
        self._ride_home()
