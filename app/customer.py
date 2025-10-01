from dataclasses import dataclass
from typing import Dict, List
from math import dist
from .car import Car
from .shop import Shop

@dataclass
class Customer:
    name: str
    product_cart: Dict[str, int]
    location: List[int]
    money: float
    car: Car
    home: List[int] = None

    def __post_init__(self):
        # сохраняем "дом" (начальные координаты)
        self.home = list(self.location)

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        """Стоимость поездки туда и обратно + покупки."""
        d_to_shop = dist(self.location, shop.location)
        d_home = dist(shop.location, self.home)
        fuel_to_shop = self.car.fuel_cost(d_to_shop, fuel_price)
        fuel_home = self.car.fuel_cost(d_home, fuel_price)
        products = shop.calculate_cart_price(self.product_cart)
        return round(fuel_to_shop + products + fuel_home, 2)

    def ride_to_shop(self, shop: Shop):
        self.location = list(shop.location)

    def ride_home(self):
        self.location = list(self.home)
