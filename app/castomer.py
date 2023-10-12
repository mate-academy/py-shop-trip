from typing import Dict, Any
from app.shop import Shop
from app.car import Car


class Customer:
    def __init__(
            self,
            info: Dict[str, Any],
            fuel_price: float
    ) -> None:
        self.name = info["name"]
        self.product_cart = info["product_cart"]
        self.location = info["location"]
        self.home_location = info["location"]
        self.money = info["money"]
        self.car = Car(info.get("car", {}), fuel_price)

    def calculate_trip_cost(
            self,
            fuel_price: float,
            shop: Shop
    ) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        fuel_cost = (distance / 100) * \
            self.car.fuel_consumption * fuel_price * 2
        products_cost = self.calculate_products_cost(shop)
        total = round(products_cost + fuel_cost, 2)
        return total

    def calculate_products_cost(
            self,
            shop: Shop,
    ) -> float | int:
        products_cost = sum(amount * shop.products[product] for
                            product, amount in self.product_cart.items()
                            if product in shop.products)
        return round(products_cost, 2)
