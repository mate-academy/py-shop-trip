from math import sqrt
from typing import TYPE_CHECKING

from app.car import Car

if TYPE_CHECKING:
    from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            products: dict,
            location: list[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.products = products
        self.location = location
        self.home_location = location
        self.money = money
        self.car = car

    def dist_to_location(self, location: list[int]) -> float:
        return sqrt(
            (location[0] - self.location[0]) ** 2
            + (location[1] - self.location[1]) ** 2
        )

    def get_trip_cost(self, shop: Shop, fuel_cost: float) -> float:
        # fuel = consumption/100 * 2*dist * fuel_price
        fuel_cost = (self.car.fuel_consumption / 100
                     * 2 * self.dist_to_location(shop.location)
                     * fuel_cost)
        product_prices = shop.products
        products_cost = 0
        for product, quantity_to_buy in self.products.items():
            if product in product_prices:
                products_cost += product_prices[product] * quantity_to_buy

        return fuel_cost + products_cost

    def ride(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location
        print(shop.get_purchase_receipt(self))
        print(f"{self.name} rides home")
        self.location = self.home_location
