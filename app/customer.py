import datetime

from app.car import Car
from app.shop import Shop
from app.utils import (count_distance_between_locations,
                       shop_cart_cost, format_price)


class Customer:
    def __init__(self, name: str, product_cart: dict, location: list,
                 money: int, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = self.location.copy()

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"

    def _fuel_cost_for_shop(self, shop: Shop, fuel_price: float) -> float:
        km = count_distance_between_locations(self.location, shop.location)
        fuel_cost = km / 100 * self.car.fuel_consumption * 2 * fuel_price
        return round(fuel_cost, 2)

    def total_cost_for_shop(self, shop: Shop, fuel_price: float) -> float:
        fuel = self._fuel_cost_for_shop(shop, fuel_price)
        products = shop_cart_cost(self.product_cart, shop.products)
        return fuel + products

    def ride_to_shop(self, shop: Shop) -> None:
        self.location = shop.location
        print(f"Date: {datetime.datetime.now().strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0.0
        for product, qty in self.product_cart.items():
            cost = shop.products.get(product, 0) * qty
            print(f"{qty} {product}s for {format_price(cost)} dollars")
            total_cost += cost
        print(f"Total cost is {format_price(total_cost)} dollars")
        print("See you again!")
        print("")
