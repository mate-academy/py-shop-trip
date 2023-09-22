from typing import Dict, Any, List
from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(self, info: Dict[str, Any], fuel_price: float) -> None:
        self.name = info["name"]
        self.product_cart = info["product_cart"]
        self.location = info["location"]
        self.home_location = info["location"]
        self.money = info["money"]
        self.car = Car(info.get("car", {}), fuel_price)

    def calculate_products_cost(self, shop: Shop) -> float | int:
        products_cost = 0
        for product, amount in self.product_cart.items():
            if product in shop.products:
                products_cost += amount * shop.products[product]
        return round(products_cost, 2)

    def calculate_distance_to_shop(self, shop_location: List) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return round(distance, 2)

    def calculate_trip_cost(self, shop: Shop) -> float:
        distance = self.calculate_distance_to_shop(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance)
        products_cost = self.calculate_products_cost(shop)
        total = round(products_cost + fuel_cost, 2)
        return total
