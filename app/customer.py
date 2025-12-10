from math import dist
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        location: list,
        money: float,
        car: Car,
        product_cart: dict
    ) -> None:
        self.name = name
        self.location = tuple(location)
        self.money = money
        self.product_cart = product_cart
        if isinstance(car, dict):
            self.car = Car(**car)
        else:
            self.car = car

    def distance_to(self, shop_location: tuple) -> float:
        return dist(self.location, shop_location)

    def total_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        fuel_cost = self.car.trip_cost(distance * 2, fuel_price)
        if not shop.can_fulfill(self.product_cart):
            return float("inf")
        product_cost = shop.total_price(self.product_cart)
        return fuel_cost + product_cost

    def go_to_shop(self, location: tuple) -> None:
        self.location = location

    def go_to_home(self) -> None:
        self.location = self.location

    def visit_shop(self, shop: Shop, fuel_price: float) -> None:
        distance = self.distance_to(shop.location)
        round_trip_cost = self.car.trip_cost(distance * 2, fuel_price)
        products_cost = shop.total_price(self.product_cart)
        total_cost = round_trip_cost + products_cost

        print(f"{self.name} rides to {shop.name}")
        self.go_to_shop(shop.location)

        shop.print_receipt(self.name, self.product_cart)

        self.money -= total_cost
        self.go_to_home()
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money:.2f} dollars\n")
