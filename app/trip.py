from __future__ import annotations
import math
from typing import List
from importlib import import_module


class Trip:

    def __init__(
        self,
        shop_name: str,
        shop_location: list,
        trip_price: float,
        total_milk_cost: float,
        total_bread_cost: float,
        total_butter_cost: float
    ) -> None:
        self.shop_name = shop_name
        self.shop_location = shop_location
        self.trip_price = trip_price
        self.total_milk_cost = total_milk_cost
        self.total_bread_cost = total_bread_cost
        self.total_butter_cost = total_butter_cost
        self.total_product_price = sum(
            [total_milk_cost, total_bread_cost, total_butter_cost]
        )
        self.total_trip = self.trip_price + self.total_product_price

    @staticmethod
    def cheapest_trip(trips: List[Trip]) -> Trip:
        return min(trips, key=lambda obj: obj.total_trip)

    @staticmethod
    def trip_distance(
        shop_location: List[int],
        customer_location: List[int]
    ) -> float:
        return math.sqrt(
            (shop_location[0] - customer_location[0]) ** 2
            + (shop_location[1] - customer_location[1]) ** 2
        )

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

    @staticmethod
    def choose_shop_and_go_to_trip(
        customer_instances: list,
        shop_instances: list
    ) -> None:
        class_customer = import_module("app.customer").Customer
        class_shop = import_module("app.shop").Shop

        for customer in customer_instances:
            trip_instances = []

            for shop in shop_instances:
                trip_distance = Trip.trip_distance(
                    shop_location=shop.location,
                    customer_location=customer.location
                )

                trip_price = Trip.trip_price(
                    fuel_consumption=customer.car.fuel_consumption,
                    fuel_price=customer.car.fuel_price,
                    trip_distance=trip_distance
                )

                total_milk_cost = (
                    customer.product_cart["milk"] * shop.products["milk"]
                )
                total_bread_cost = (
                    customer.product_cart["bread"] * shop.products["bread"]
                )
                total_butter_cost = (
                    customer.product_cart["butter"] * shop.products["butter"]
                )
                trip_instances.append(
                    Trip(
                        shop_name=shop.name,
                        shop_location=shop.location,
                        trip_price=trip_price,
                        total_milk_cost=total_milk_cost,
                        total_bread_cost=total_bread_cost,
                        total_butter_cost=total_butter_cost
                    )
                )

            if not class_customer.customer_chose_shop(
                customer=customer,
                trip_instances=trip_instances
            ):
                continue

            class_shop.shop_receipt(
                customer=customer,
                trip_instances=trip_instances
            )

            class_customer.customer_rides_home(
                customer=customer,
                trip_instances=trip_instances
            )
