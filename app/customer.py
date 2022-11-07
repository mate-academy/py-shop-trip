import math

from app.car import Car
from app.shop import Shop
from dataclasses import dataclass


@dataclass
class Customer:

    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def balance_printer(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def distance(self, shop: Shop) -> float:
        return math.dist(self.location, shop.location)

    def cost_distance(self, shop: Shop, fuel_price: float) -> float:
        return (self.distance(shop) * self.car.km_price() * fuel_price) * 2

    def cost_product(self, shop: Shop) -> dict:
        return {shop.name: {
            key: (value * self.product_cart[key])
            for key, value in shop.products.items()}}

    def product_price(self, shop: Shop) -> dict:
        return {shop: sum(products.values())
                for shop, products in self.cost_product(shop).items()}

    def total_cost(self, shops: list, fuel_price: float) -> dict:
        dict_cost_trip = {}

        for shop in shops:
            product = self.product_price(shop)[shop.name]
            fuel = self.cost_distance(shop, fuel_price)
            cost_trip = {shop.name: round(product + fuel, 2)}
            dict_cost_trip.update(cost_trip)

        return dict_cost_trip

    def best_trip(self, shops: list, fuel_price: float) -> str:
        all_prices = self.total_cost(shops, fuel_price)
        minimal = min(all_prices.values())

        for shop_name, value in all_prices.items():
            if value == minimal:
                return shop_name

    def new_balance(
            self,
            shops: list,
            fuel_price: float,
            min_trip: str) -> int:
        return self.money - self.total_cost(shops, fuel_price)[min_trip]
