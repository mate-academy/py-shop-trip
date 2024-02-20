from __future__ import annotations
from app.car import Car
from app.trip import Trip
from typing import List


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[int],
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @staticmethod
    def customer_chose_shop(
            customer: Customer,
            trip_instances: List[Trip]
    ) -> bool:
        cheapest_trip = Trip.cheapest_trip(trip_instances)
        print(f"{customer.name} has {customer.money} dollars")

        for shop in trip_instances:
            print(
                f"{customer.name}'s trip to the "
                f"{shop.shop_name} costs {round(shop.total_trip, 2)}"
            )

        if customer.money < cheapest_trip.total_trip:
            print(
                f"{customer.name} doesn't have enough "
                f"money to make a purchase in any shop")
            return False

        print(f"{customer.name} rides to {cheapest_trip.shop_name}\n")
        return True

    @staticmethod
    def customer_rides_home(
            customer: Customer,
            trip_instances: List[Trip]
    ) -> None:
        cheapest_trip = Trip.cheapest_trip(trip_instances)
        print(
            f"{customer.name} rides home\n"
            f"{customer.name} now has "
            f"{round(customer.money - cheapest_trip.total_trip, 2)} "
            f"dollars\n"
        )
