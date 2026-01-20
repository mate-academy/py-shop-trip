from __future__ import annotations

from app.car import Car
from app.trip import Trip


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = []

    def add_home_location(self, location: list) -> None:
        self.home_location.clear()
        self.home_location.append(location)

    def get_home_location(self) -> list:
        return self.home_location[0] if self.home_location else []

    def chose_shop(self, trip_instances: list) -> bool:
        cheapest_trip = Trip.cheapest_trip(trip_instances)
        print(f"{self.name} has {self.money} dollars")
        for shop in trip_instances:
            print(
                f"{self.name}'s trip to the "
                f"{shop.shop_name} costs {round(shop.total_trip, 2)}"
            )
        if self.money < cheapest_trip.total_trip:
            print(
                f"{self.name} doesn't have enough "
                f"money to make a purchase in any shop")
            return False
        self.add_home_location(self.location)
        self.location = cheapest_trip.shop_location
        print(f"{self.name} rides to {cheapest_trip.shop_name}\n")
        return True

    def rides_home(self, cheapest_trip: Trip) -> None:
        self.location = self.get_home_location()
        print(
            f"{self.name} rides home\n"
            f"{self.name} now has "
            f"{round(self.money - cheapest_trip.total_trip, 2)} "
            f"dollars\n"
        )

    def choose_shop_and_go_to_trip(self, shop_instances: dict) -> None:
        trip_instances = []
        for shop in shop_instances.values():
            trip_distance = Trip.trip_distance(
                shop.location,
                self.location
            )
            trip_price = Trip.trip_price(
                self.car.fuel_consumption,
                self.car.fuel_price,
                trip_distance
            )
            total_products_cost = shop.total_products_cost(self)
            trip_instances.append(
                Trip(
                    shop.name,
                    shop.location,
                    trip_price,
                    total_products_cost
                )
            )
        if not self.chose_shop(
            trip_instances
        ):
            return
        cheapest_trip = Trip.cheapest_trip(trip_instances)
        cheapest_shop = shop_instances[cheapest_trip.shop_name]
        cheapest_shop.shop_receipt(
            self,
            cheapest_trip
        )
        self.rides_home(
            cheapest_trip
        )
