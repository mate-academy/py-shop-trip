import math
from app.car import Car


class Customer:
    def __init__(
            self, name: str,
            cart: dict,
            location: list,
            money: float,
            car: Car
    ) -> None:
        self.name = name
        self.cart = cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = location[:]

    def distance_to(self, shop) -> float:
        x1, y1 = self.location
        x2, y2 = shop.location
        return math.dist([x1, y1], [x2, y2])

    def trip_cost(self, shop, fuel_price: float) -> float:
        dist = self.distance_to(shop)
        fuel_to_and_back = self.car.fuel_cost(dist, fuel_price) * 2
        products_cost = shop.calculate_cart_cost(self.cart)
        return fuel_to_and_back + products_cost

    def can_afford(self, cost: float) -> bool:
        return self.money >= cost

    def go_to(self, shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location[:]

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location[:]
