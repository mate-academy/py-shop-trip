import dataclasses
import math

from app.car import Car
from app.shop import Shop
from app.utils import format_money


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict[str, int]
    location: list[int]
    money: float
    car: Car

    @classmethod
    def from_dict(cls, data: dict) -> "Customer":
        """Build a Customer instance from the config dictionary."""
        return cls(
            name=data["name"],
            product_cart=data["product_cart"],
            location=data["location"],
            money=data["money"],
            car=Car(**data["car"]),
        )

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        """Fuel there and back plus the cost of all products."""
        distance = math.dist(self.location, shop.location)
        fuel_cost = self.car.calculate_fuel_cost(distance, fuel_price) * 2

        return fuel_cost + shop.calculate_products_cost(self.product_cart)

    def make_trip(self, shops: list[Shop], fuel_price: float) -> None:
        """Choose the cheapest shop and go there if there is enough money."""
        print(f"{self.name} has {format_money(self.money)} dollars")

        trips = [
            (shop, self.calculate_trip_cost(shop, fuel_price))
            for shop in shops
        ]

        for shop, trip_cost in trips:
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {format_money(trip_cost)}"
            )

        cheapest_shop, cheapest_cost = min(trips, key=lambda trip: trip[1])

        if cheapest_cost > self.money:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            return

        home_location = self.location
        print(f"{self.name} rides to {cheapest_shop.name}")
        self.location = cheapest_shop.location

        cheapest_shop.print_receipt(self.name, self.product_cart)

        print(f"{self.name} rides home")
        self.location = home_location
        self.money -= cheapest_cost
        print(f"{self.name} now has {format_money(self.money)} dollars")
