from __future__ import annotations
import math


class Trip:
    def __init__(
        self,
        shop_name: str,
        shop_location: list,
        trip_price: float,
        total_products_cost: dict
    ) -> None:
        self.shop_name = shop_name
        self.shop_location = shop_location
        self.trip_price = trip_price
        self.total_products_cost = total_products_cost
        self.total_product_price = sum(
            total_products_cost.values()
        )
        self.total_trip = self.trip_price + self.total_product_price

    @staticmethod
    def cheapest_trip(trips: list) -> Trip:
        return min(trips, key=lambda obj: obj.total_trip)

    @staticmethod
    def trip_distance(
        shop_location: list,
        customer_location: list
    ) -> float:
        return math.dist(customer_location, shop_location)

    @staticmethod
    def trip_price(
        fuel_consumption: float,
        fuel_price: float,
        trip_distance: float
    ) -> float:
        return (
            fuel_consumption
            * fuel_price
            * trip_distance / 100
        ) * 2
