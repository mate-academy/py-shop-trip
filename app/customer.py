from typing import Tuple, Dict
from app.car import Car
from app.shop import Shop


class Customer:

    def __init__(self, name: str, product_cart: Dict[str, int],
                 location: Tuple[int, int], money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop_location: Tuple[int, int]) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def calculate_trip_cost(self, shop_location: Tuple[int, int],
                            fuel_price: float) -> float:
        distance = self.calculate_distance(shop_location)
        return (distance * (self.car.fuel_consumption / 100) * fuel_price) * 2

    def calculate_product_cost(self, shop_products: Dict[str, float]) -> float:
        total_cost = 0
        for product, qty in self.product_cart.items():
            if product in shop_products:
                total_cost += round(shop_products[product] * qty, 2)
        return total_cost

    def calculate_total_cost(self, shop: Shop, fuel_price: float) -> float:
        trip_cost = self.calculate_trip_cost(shop.location, fuel_price)
        product_cost = self.calculate_product_cost(shop.products)
        return round(trip_cost + product_cost, 2)

    def update_location(self, new_location: Tuple[int, int]) -> None:
        self.location = new_location

    def return_home(self) -> None:
        self.location = self.home_location
