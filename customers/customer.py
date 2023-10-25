import json

from app.shop import Shop
from customers.car import Car


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop_location: list) -> float:
        difference_x = (shop_location[0] - self.location[0]) ** 2
        difference_y = (shop_location[1] - self.location[1]) ** 2
        return (difference_x + difference_y) ** 0.5

    def calculate_buys(self, shop: Shop, data: json) -> int | float:
        buy_milk = self.product_cart.get("milk") * shop.products["milk"]
        buy_bread = self.product_cart.get("bread") * shop.products["bread"]
        buy_butter = self.product_cart.get("butter") * shop.products["butter"]
        distance = self.calculate_distance(shop.location)
        trip_cost = self.car.calculate_trip_coast(distance, data)
        return buy_milk + buy_butter + buy_bread + trip_cost * 2
