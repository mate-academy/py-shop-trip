import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def distance_to(self, location: list) -> float:
        return math.dist(self.location, location)

    def fuel_cost(self, distance: float, fuel_price: float) -> float:
        return (distance / 100) * self.car.fuel_consumption * fuel_price

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)

        fuel_to_shop = self.fuel_cost(distance, fuel_price)
        fuel_back = fuel_to_shop

        products_cost = shop.calculate_products_cost(self.product_cart)

        return fuel_to_shop + fuel_back + products_cost

    def enough_money(self, cost: float) -> bool:
        return self.money >= cost

    def pay(self, cost: float) -> float:
        self.money -= cost
        return round(self.money, 2)

    def __str__(self) -> str:
        return self.name
