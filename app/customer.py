from typing import Optional

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name, location, money, cart, car: Car) -> None:
        self.name = name
        self.location = tuple(location)
        self.money = float(money)
        self.cart = dict(cart)
        self.car = car

    def evaluate_shop(self, shop: Shop, fuel_price: float) -> Optional[float]:
        products_cost = shop.products_cost(self.cart)
        if products_cost is None:
            return None

        dist = shop.distance_to(self.location)
        fuel_cost = self.car.fuel_cost_for_distance(dist * 2, fuel_price)
        return products_cost + fuel_cost

    def go_to_shop(self, shop: Shop, fuel_price: float) -> bool:
        total = self.evaluate_shop(shop, fuel_price)
        if total is None or total > self.money:
            return False

        home = self.location
        self.location = shop.location
        shop.print_receipt(self.name, self.cart)
        self.location = home

        self.money -= total
        return True
