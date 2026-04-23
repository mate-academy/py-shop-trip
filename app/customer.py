import math

from app.car import Car
from app.shop import Shop


def fmt(num: float) -> float | int:
    rounded = round(num, 2)
    return int(rounded) if rounded == int(rounded) else rounded


class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.product_cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = Car(data["car"]["brand"], data["car"]["fuel_consumption"])

    def calculate_distance(self, target_location: list) -> float:
        return math.sqrt(
            (self.location[0] - target_location[0]) ** 2
            + (self.location[1] - target_location[1]) ** 2
        )

    def get_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        dist = self.calculate_distance(shop.location)
        fuel_cost = (dist * 2) * (self.car.fuel_consumption / 100) * fuel_price
        product_cost = shop.calculate_products_cost(self.product_cart)
        return fuel_cost + product_cost

    def shop_trip(self, shops: list[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {fmt(self.money)} dollars")

        cheapest_shop = None
        lowest_cost = float("inf")

        for shop in shops:
            cost = self.get_trip_cost(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {fmt(cost)}")
            if cost < lowest_cost:
                lowest_cost = cost
                cheapest_shop = shop

        if lowest_cost <= self.money:
            print(f"{self.name} rides to {cheapest_shop.name}\n")

            home_location = self.location
            self.location = cheapest_shop.location

            cheapest_shop.print_receipt(self)
            self.money -= lowest_cost

            self.location = home_location
            print(f"\n{self.name} rides home")
            print(f"{self.name} now has {fmt(self.money)} dollars")
        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
