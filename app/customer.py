from __future__ import annotations

import datetime
from decimal import Decimal

from app.car import Car
from app.location import Location
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int | float],
            location: Location,
            money: int | float,
            car: Car,
            home_location: Location | None = None
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = home_location or location

    @classmethod
    def from_dict(cls, customer: dict) -> Customer:
        return cls(
            name=customer.get("name"),
            product_cart=customer.get("product_cart"),
            location=Location(customer.get("location")),
            money=customer.get("money"),
            car=Car.from_dict(customer.get("car"))
        )

    def get_trip_cost_to(self, shop: Shop, fuel_price: float) -> float:
        fuel_cost = self.car.get_trip_cost(
            self.location.distance_to(shop.location),
            fuel_price
        )
        product_cost = shop.total_cost_of(self.product_cart)
        return product_cost + fuel_cost * 2

    def ride_to(self, shop: Shop, fuel_price: float) -> None:
        print(f"{self.name} rides to {shop.name}\n")

        self.money -= self.car.get_trip_cost(
            self.location.distance_to(shop.location),
            fuel_price
        )

        self.location = shop.location

    def buy_products_in(self, shop: Shop) -> None:
        current_time = datetime.datetime.now()
        time_string = current_time.strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {time_string}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, amount in self.product_cart.items():
            if product in shop.products:
                product_cost = amount * shop.products[product]
                total_cost += product_cost
                normalized_cost = Decimal(str(product_cost)).normalize()
                print(f"{amount} {product}s for {normalized_cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

        self.money -= total_cost

    def return_home(self, fuel_price: float) -> None:
        print(f"{self.name} rides home")

        self.money -= self.car.get_trip_cost(
            self.location.distance_to(self.home_location),
            fuel_price
        )

        print(f"{self.name} now has {round(self.money, 2)} dollars\n")

        self.location = self.home_location

    def choose_shop(self, shops: list[Shop], fuel_price: float) -> Shop | None:
        print(f"{self.name} has {round(self.money, 2)} dollars")
        if not shops:
            return None

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            try:
                trip_cost = self.get_trip_cost_to(shop, fuel_price)
                print(
                    f"{self.name}'s trip to the {shop.name} "
                    f"costs {round(trip_cost, 2)}"
                )
                if trip_cost < min_trip_cost:
                    cheapest_shop = shop
                    min_trip_cost = trip_cost
            except KeyError as err:
                print(err)

        if min_trip_cost > self.money:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            return None

        return cheapest_shop

    def make_purchases(self, shops: list[Shop], fuel_price: float) -> None:
        cheapest_shop = self.choose_shop(shops, fuel_price)
        if cheapest_shop is not None:
            self.ride_to(cheapest_shop, fuel_price)
            self.buy_products_in(cheapest_shop)
            self.return_home(fuel_price)
