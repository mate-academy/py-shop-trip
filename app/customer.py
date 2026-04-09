import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list[int],
        money: float | int,
        car_data: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.home_location = location
        self.car = Car(car_data["brand"], car_data["fuel_consumption"])

    def calculate_trip(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(self.location, shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price) * 2
        products_cost = shop.get_product_price(self.product_cart)
        return round(fuel_cost + products_cost, 2)
