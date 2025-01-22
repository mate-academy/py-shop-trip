from dataclasses import dataclass
from app.car import Car
from math import sqrt
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: Car

    def calculate_distance_from_home_to_shop(
            self, shop_location: list[int]
    ) -> int | float:
        distance = sqrt((shop_location[0] - self.location[0]) ** 2
                        + (shop_location[1] - self.location[1]) ** 2)
        return round(distance * 2, 2)

    def calculate_trip_cost(
            self, shop: Shop, fuel_price: float
    ) -> int | float:
        distance = self.calculate_distance_from_home_to_shop(shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price)
        products_cost = shop.products_cost(self.product_cart)
        return round(fuel_cost + products_cost, 2)
