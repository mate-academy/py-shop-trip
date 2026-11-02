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

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        fuel = self.car.fuel_cost(distance, fuel_price)
        return fuel * 2 + shop.cart_cost(self.product_cart)

    def go_shopping(self, shops: list, fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        costs = {}
        for shop in shops:
            costs[shop.name] = self.trip_cost(shop, fuel_price)
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {round(costs[shop.name], 2)}"
            )

        cheapest = min(shops, key=lambda shop: costs[shop.name])
        cost = costs[cheapest.name]

        if cost > self.money:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            return

        home = self.location
        print(f"{self.name} rides to {cheapest.name}")
        self.location = cheapest.location
        cheapest.print_receipt(self.name, self.product_cart)

        print(f"{self.name} rides home")
        self.location = home
        self.money = round(self.money - cost, 2)
        print(f"{self.name} now has {self.money} dollars")
