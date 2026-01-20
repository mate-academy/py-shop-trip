import math
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: int, car: "Car") -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.best_total_cost = None
        self.best_shop = None

    def distance_to(self, shop: Shop) -> float:
        result = [a - b for a, b in zip(self.location, shop.location)]
        return round(math.sqrt(pow(result[0], 2) + pow(result[1], 2)), 2)

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        return round(2 * self.car.cost(self.distance_to(shop), fuel_price), 2)

    def can_afford(self, shop: Shop, fuel_price: float) -> bool:
        if self.money >= ((self.trip_cost(shop, fuel_price)
                           + self.best_total_cost)):
            return True
        return False

    def go_to(self, point: list) -> None:
        if point == self.location:
            print(f"{self.name} rides home")
        else:
            print(f"{self.name} rides to {self.best_shop}\n")
