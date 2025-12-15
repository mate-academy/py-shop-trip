from dataclasses import dataclass
from typing import List, Dict
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int]
    home_location: List[float]
    current_location: List[float]
    money: float
    car: Car

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = shop.calculate_distance(self.current_location)
        return self.car.calculate_trip_cost(distance * 2, fuel_price)

    def calculate_products_price(self, shop: Shop) -> float | int:
        return sum(shop.get_product_price(product)
                   * quantity for product, quantity
                   in self.product_cart.items())

    def get_full_price(self, shop: Shop, fuel_price: float) -> float:
        trip_cost = self.calculate_trip_cost(shop, fuel_price)
        products_cost = self.calculate_products_price(shop)
        return trip_cost + products_cost

    def can_afford_trip(self, shop: Shop, fuel_price: float) -> bool:
        return self.money >= self.get_full_price(shop, fuel_price)

    def make_purchase(self, shop: Shop, fuel_price: float) -> bool:
        if self.can_afford_trip(shop, fuel_price):
            self.money -= self.get_full_price(shop, fuel_price)
            self.current_location = shop.location
            return True
        return False

    def go_back(self) -> None:
        self.current_location = self.home_location
