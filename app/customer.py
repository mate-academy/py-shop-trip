import datetime
from typing import Any, Dict, List, Union

from app.car import Car
from app.shop import Shop


def format_number(value: float) -> Union[int, float]:
    value = round(value, 2)
    return int(value) if value == int(value) else value


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str, int],
            location: List[float],
            money: float,
            car: Dict[str, Any]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])

    def process_shopping(self, shops: List[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")

        trips = []
        for shop in shops:
            cost = shop.calculate_trip_cost(self, fuel_price)
            trips.append((shop, cost))
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")

        affordable = [(s, c) for s, c in trips if c <= self.money]
        if not affordable:
            print(
                f"{self.name} doesn't have enough "
                "money to make a purchase in any shop"
            )
            return

        shop, cost = min(affordable, key=lambda item: item[1])
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location

        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total = 0.0
        for product, qty in self.product_cart.items():
            item_cost = qty * shop.products[product]
            total += item_cost
            print(f"{qty} {product}s for {format_number(item_cost)} dollars")

        print(f"Total cost is {format_number(total)} dollars")
        print("See you again!\n")

        print(f"{self.name} rides home")
        self.money = round(self.money - cost, 2)
        print(f"{self.name} now has {format_number(self.money)} dollars\n")
