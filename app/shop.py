from decimal import Decimal
from math import sqrt

from app.car import Car


class Shop:
    def __init__(self, name: str, products: dict, location: tuple) -> None:
        self.name = name
        self.products = products
        self.location = location

    def cost_for_products(self, product_cart: dict) -> Decimal:
        total = Decimal("0.00")
        for product, quantity in product_cart.items():
            if product in self.products:
                total += Decimal(quantity) * Decimal(self.products[product])
        return total

    @staticmethod
    def cost_of_fuel(
            location: tuple,
            shop_location: tuple,
            car: Car
    ) -> Decimal:
        distance = Decimal(sqrt((shop_location[0] - location[0])
                                ** 2 + (shop_location[1] - location[1]) ** 2))
        amount_of_liters_per_distance = (distance * car.consumption
                                         / Decimal("100"))
        return amount_of_liters_per_distance * car.fuel_price * Decimal("2")

    @staticmethod
    def total_cost_for_every_shop(
            shops: list,
            product_cart: dict,
            location: tuple,
            car: Car
    ) -> dict:
        full_cost_every_shop = {}
        for shop_data in shops:
            shop = Shop(**shop_data)
            product_cost = shop.cost_for_products(product_cart)
            fuel_cost = Shop.cost_of_fuel(location, shop.location, car)
            full_cost_every_shop[shop.name] = product_cost + fuel_cost
        return full_cost_every_shop

    @staticmethod
    def get_shop_by_name(shops: list, shop_name: str) -> None:
        return next(
            (shop for shop in shops if shop["name"] == shop_name), None)
