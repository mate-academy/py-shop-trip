import math
from dataclasses import dataclass
from typing import List


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    def find_cheapest_trip_to_shop(self, shops: list, fuel_price: float):
        cheapest_trip = {"cost": float("inf"),
                         "shop": None}

        for shop in shops:
            fuel_consumption = self.car["fuel_consumption"]
            road_cost = Customer.cost_of_trip_to_shop(
                self.location, shop.location,
                fuel_consumption, fuel_price,
            )
            product_cost = shop.cost_of_products_in_shop(self.product_cart)
            trip_cost = round(road_cost + product_cost, 2)

            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")

            if trip_cost < cheapest_trip["cost"]:
                cheapest_trip["cost"] = trip_cost
                cheapest_trip["shop"] = shop
        return cheapest_trip

    @staticmethod
    def cost_of_trip_to_shop(current_location: List[int],
                             shop_location: List[int],
                             fuel_consumption: float,
                             fuel_price: float
                             ):
        distance_to_shop = math.dist(current_location, shop_location)
        liter_per_km = fuel_consumption / 100
        road_cost = distance_to_shop * liter_per_km * fuel_price * 2
        return round(road_cost, 2)

    def ride_to_shop(self, cheapest_trip: dict):
        shop = cheapest_trip["shop"]
        home = self.location
        self.location = shop.location
        shop.shopping(self)
        self.money = round(self.money - cheapest_trip["cost"], 2)
        print(f"{self.name} rides home")
        self.location = home
