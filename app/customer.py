from datetime import datetime
from math import dist

from app.car import Car
from app.shop import Shop
from app.car import FUEL_PRICE


class Customer:
    _all_customers = []

    def __init__(
            self,
            name: str,
            products: dict[str: int],
            location: list[int, int],
            money: float,
            car: Car
    ) -> None:
        self._name = name
        self._products = products
        self._location = location
        self._money = money
        self._car = car

    def __str__(self) -> str:
        return (f"{self._name} has {self.money}$, "
                f"wants to buy {self.products}, has a {self._car}")

    @property
    def name(self) -> str:
        return self._name

    @property
    def products(self) -> list:
        return self._products

    @property
    def location(self) -> list[int, int]:
        return self._location

    @property
    def money(self) -> float:
        return self._money

    @money.setter
    def money(self, new_value: float) -> None:
        self._money -= new_value

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
        for name, count in self.products.items():
            total_price += shop.products[name].price * count
        return round(total_price, 2)

    def cost_drive(self, location: Shop) -> float:
        # d = sqrt((x2 - x1)^2 + (y2 - y1)^2)
        distance_in_km = dist(self.location, location.location)
        cost = (distance_in_km
                * 2 * self._car.fuel_consumption_in_km * FUEL_PRICE)
        return round(cost, 2)

    def buy_products(self, shop: Shop) -> None:
        print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought:")
        total_price = self.cost_products_in_shop(shop)

        self.cost_products_in_shop(shop)
        for name, count in self.products.items():
            print(f"{count} {name}s for "
                  f"{shop.products[name].price * count} dollars")

        print(f"Total cost is {total_price} dollars")
        print("See you again!\n")

    def ride_shop(self, shop: Shop) -> None:
        self._location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def start_trip(self, shop: Shop) -> None:
        self.ride_shop(shop)
        self.buy_products(shop)
        self.ride_home()
