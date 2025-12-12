from typing import Dict, Tuple
from app.utils import distance
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: Dict[str, int],
        location: Tuple[float, float],
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = tuple(location)
        self.home_location = tuple(location)
        self.money = money
        self.car = car

    def total_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        one_way = distance(self.home_location, shop.location)
        fuel_cost = self.car.fuel_cost(one_way * 2, fuel_price)
        products_cost = shop.cart_cost(self.product_cart)
        return fuel_cost + products_cost

    def go_to(self, location: Tuple[float, float]) -> None:
        self.location = tuple(location)

    def go_home(self) -> None:
        self.location = self.home_location
