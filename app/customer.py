from typing import Tuple

from app.car import Car
from app.shop import Shop


class Customer:
    all_customers = []

    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.location = customer["location"]
        self.money = customer["money"]
        self.product_cart = customer["product_cart"]
        self.car = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        self.home = customer["location"]

        Customer.all_customers.append(self)

    def choice_cheap_shoping(self, shops: list[Shop]) -> tuple[Shop, float] | \
                                                         tuple[None, None]:
        print(f"{self.name} has {self.money} dollars")
        trip_options = {}

        if len(shops) == 0:
            raise ValueError("The list of shops is empty")

        for shop in shops:
            fuel_total_cost = self.car.calculate_cost_travel(
                self.location,
                shop.location
            )

            product_cost = shop.total_purchase_cost(self.product_cart)
            trip_options[shop] = product_cost + fuel_total_cost
        for shop, cost in trip_options.items():
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")

        best_shop = min(trip_options, key=lambda x: trip_options[x])
        if trip_options[best_shop] <= self.money:
            return best_shop, trip_options[best_shop]
        else:
            print(f"{self.name} doesn't have enough money to make a purchase "
                  f"in any shop")
            return None, None

    def remaining_money(self, total_cost: float) -> None:
        remaining_money = self.money - total_cost
        print(
            f"{self.name} now has {remaining_money} dollar{'s' if remaining_money == 1 else 's'}\n")

