import math
from app.car import Car
from app.shop import Shop


def distance(loc1: list, loc2: list) -> float:
    return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car = car
        self.home_location = location.copy()

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:

        dist_to_shop = distance(self.location, shop.location)
        dist_round_trip = dist_to_shop * 2
        fuel_cost = self.car.calculate_fuel_cost(dist_round_trip, fuel_price)
        product_cost = shop.calculate_product_cost(self.product_cart)
        return fuel_cost + product_cost

    def travel_to_shop(self, shop: Shop, fuel_price: float) -> None:

        trip_cost = self.calculate_trip_cost(shop, fuel_price)
        self.money -= trip_cost
        self.location = shop.location.copy()
        print(
            f"{self.name} travelled to {shop.name} and spent {trip_cost:.2f} "
            f"on travel and purchases. "
            f"Remaining balance: {self.money:.2f} dollars."
        )

    def return_home(self, fuel_price: float) -> None:

        dist_to_home = distance(self.location, self.home_location)
        fuel_cost = self.car.calculate_fuel_cost(dist_to_home, fuel_price)
        self.money -= fuel_cost
        self.location = self.home_location.copy()
        print(
            f"{self.name} returned home and now has {self.money:.2f} dollars "
            f"(spent {fuel_cost:.2f} on fuel).\n"
        )

    def go_to(self, location: list) -> None:
        self.location = location
