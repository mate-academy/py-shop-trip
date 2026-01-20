import math
from car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            money: float,
            product_cart: dict,
            location: list[int, int],
            car: Car
    ) -> None:
        self.name = name
        self.money = money
        self.product_cart = product_cart
        self.location = location
        self.car = car

    def distance_to(self, shop: Shop) -> float:
        return round(math.sqrt(
            (self.location[0] - shop.location[0])
            ** 2 + (self.location[1] - shop.location[1]) ** 2), 2)

    def can_afford_trip(self, shop: Shop, fuel_price: float) -> bool:
        trip_distance = self.distance_to(shop) * 2
        trip_cost = self.car.trip_cost(trip_distance, fuel_price)
        products_cost = shop.calculate_products_cost(self.product_cart)

        return trip_cost + products_cost <= self.money

    def ride_to(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}")
        self.location = shop.location

    def ride_home(self, home_location: list) -> None:
        print(f"{self.name} rides home")
        self.location = home_location

    def buy_products(self, shop: Shop, fuel_price: float) -> None:
        trip_distance = self.distance_to(shop) * 2
        trip_cost = self.car.trip_cost(trip_distance, fuel_price)
        products_cost = shop.calculate_products_cost(self.product_cart)

        total_cost = trip_cost + products_cost
        self.money -= total_cost

        shop.print_receipt(self.name, self.product_cart)
        print(f"{self.name} now has {round(self.money, 2)} dollars")
