from __future__ import annotations
from dataclasses import dataclass
from typing import List, Optional

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: List[int]
    products: dict

    def total_price(self, product_cart: dict) -> float:
        price = 0
        for product, count in product_cart.items():
            price += self.products[product] * count

        return round(price, 2)

    @staticmethod
    def list_read(shops: List[dict]) -> list:

        return [Shop(**shop) for shop in shops]

    def buy_product(self, product_cart: dict) -> None:
        total_price = 0

        for product, quantity in product_cart.items():
            price = self.products[product] * quantity
            total_price += price

            print(f"{quantity} {product}s for {price} dollars")

        print(f"Total cost is {total_price} dollars\nSee you again!\n")

    def find_best_shop(
            self: List[Shop],
            customer: Customer,
            fuel_price: float
    ) -> Optional[Shop]:
        best_shop = None
        shop_cost = None

        for shop in self:
            total_cost = customer.car.trip_fuel_cost(shop.location, fuel_price)
            total_cost += shop.total_price(customer.product_cart)

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {total_cost}"
            )

            if shop_cost is None or shop_cost > total_cost:
                best_shop = shop
                shop_cost = total_cost

        return best_shop
