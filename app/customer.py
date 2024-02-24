from __future__ import annotations
from typing import List, Tuple, Callable

from app.car import Car
from app.trip import Trip


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
    def customers_home_location(
    ) -> Tuple[Callable[[List[int]], None], Callable[[], List[int]]]:
        home_location = []

        def add_location(location: list) -> None:
            home_location.clear()
            home_location.append(location)

        def get_location() -> List:
            return home_location[0] if home_location else []
        return add_location, get_location

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

        add_location, _ = Customer.customers_home_location()
        add_location(customer.location)
        customer.location = cheapest_trip.shop_location
        print(f"{customer.name} rides to {cheapest_trip.shop_name}\n")
        return True

    @staticmethod
    def customer_rides_home(
        customer: Customer,
        trip_instances: List[Trip]
    ) -> None:
        cheapest_trip = Trip.cheapest_trip(trip_instances)
        _, get_location = Customer.customers_home_location()
        customer.location = get_location()
        print(
            f"{customer.name} rides home\n"
            f"{customer.name} now has "
            f"{round(customer.money - cheapest_trip.total_trip, 2)} "
            f"dollars\n"
        )
