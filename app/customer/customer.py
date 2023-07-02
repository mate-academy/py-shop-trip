import math

from dataclasses import dataclass
from typing import List

from app.car.car import Car
from app.shop.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int
    car: Car

    def calculate_distance(self, shop_location: List[int]) -> int | float:
        return math.sqrt((self.location[0] - shop_location[0]) ** 2
                         + (self.location[1] - shop_location[1]) ** 2)

    def calculate_cost_of_fuel(
            self,
            shop_location: List[int],
            fuel_price: float
    ) -> int | float:
        distance = self.calculate_distance(shop_location)
        return self.car.calculate_total_consumption(distance) * fuel_price

    def calculate_cost_of_product(self, shop_products: dict) -> int | float:
        cost = 0
        for product in self.product_cart:
            cost += (self.product_cart.get(product)
                     * shop_products.get(product))

        return cost

    def calculate_cost_of_trip(self, shop: Shop, fuel_price: float) -> float:
        fuel_cost = self.calculate_cost_of_fuel(shop.location, fuel_price) * 2
        product_cost = self.calculate_cost_of_product(shop.products)

        return round((fuel_cost + product_cost), 2)

    def find_cheapest_trip(
            self,
            shops: List[Shop],
            fuel_price: float
    ) -> tuple:

        cheapest_trip = None
        cheapest_shop_index = None
        cheapest_trip_cost = None

        for index, shop in enumerate(shops):
            trip_cost = self.calculate_cost_of_trip(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")

            if not cheapest_trip:
                cheapest_trip = trip_cost
                cheapest_shop_index = index
                cheapest_trip_cost = trip_cost
                continue
            if trip_cost < cheapest_trip:
                cheapest_trip = trip_cost
                cheapest_shop_index = index
                cheapest_trip_cost = trip_cost

        return shops[cheapest_shop_index], cheapest_trip_cost
