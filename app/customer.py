import math
from dataclasses import dataclass
from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: Car

    def show_yourself(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def distance_to_shop(self, shop_location: list) -> float:
        # home = self.location
        x1, y1 = self.location
        x2, y2 = shop_location

        distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
        return distance

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        fuel_one_way = self.car.fuel_cost(
            self.distance_to_shop(shop.location),
            fuel_price)
        fuel_total = fuel_one_way * 2
        products_cost = shop.products_cost(self.product_cart)

        return round(fuel_total + products_cost, 2)
