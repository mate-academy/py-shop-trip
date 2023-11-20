from __future__ import annotations
import datetime
from dataclasses import dataclass
from typing import List, Dict, Any

from app.car import Car


@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int | float]
    location: List[int]
    money: float
    car: Car

    def choose_shop(self, shops: list, fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")

        affordable_shops = []

        for shop in shops:
            distance = self.car.get_distance(self.location, shop.location)
            total_cost = round(
                shop.get_product_cost(self)
                + self.car.get_trip_cost(distance, fuel_price) * 2, 2)

            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

            if total_cost <= self.money:
                affordable_shops.append((shop, total_cost))

        if not affordable_shops:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
            return None

        affordable_shops.sort(key=lambda x: x[1])
        chosen_shop, total_cost = affordable_shops[0]
        print(f"{self.name} rides to {chosen_shop.name}")
        self.money -= total_cost
        return chosen_shop

    def make_purchase(self, chosen_shop: Any) -> None:
        print(f"\nDate: "
              f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        for product, quantity in self.product_cart.items():
            cost = round(chosen_shop.products[product] * quantity, 2)
            formatted_cost = int(cost) if cost == int(cost) else cost
            print(f"{quantity} {product}s for {formatted_cost} dollars")

        total_cost = chosen_shop.get_product_cost(self)
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

    def ride_home(self) -> None:
        print(f"\n{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
