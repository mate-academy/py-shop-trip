from __future__ import annotations
from dataclasses import dataclass, field
from typing import List


from app.car import trip_cost


@dataclass
class Customer:
    name: str
    products: dict
    location: List[int | float]
    money: int
    car: dict
    fuel_price: int | float
    cost_trip_to_shop: dict = field(default_factory=dict)

    def total_cost_to_shop(self, shop: "Shop") -> int | float:
        total_cost = sum(amount * shop.products[product]
                         for product, amount in self.products.items())
        total_cost += trip_cost(self, shop)

        if self.money - total_cost >= 0:

            self.cost_trip_to_shop[total_cost] = {
                                                  "name": shop.name,
                                                  "location": shop.location,
                                                  "products": shop.products
                                                  }

        return round(total_cost, 2)

    def the_best_shop(self) -> dict | None:
        warning = (
            f"{self.name} doesn't have "
            f"enough money to make a purchase in any shop"
        )
        best_shop = min(self.cost_trip_to_shop, default=warning)

        if isinstance(best_shop, str):
            print(best_shop)
            return

        best_shop = self.cost_trip_to_shop[best_shop]
        print(f"{self.name} rides to {best_shop['name']}\n")
        return best_shop
