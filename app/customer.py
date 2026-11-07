import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int],
        money: float,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def get_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = math.dist(self.location, shop.location)
        fuel_cost = self.car.get_fuel_cost(distance, fuel_price)

        return 2 * fuel_cost + shop.get_cart_cost(self.product_cart)

    def go_shopping(self, shops: list[Shop], fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")

        trips = []
        for shop in shops:
            trip_cost = self.get_trip_cost(shop, fuel_price)
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {round(trip_cost, 2)}"
            )
            trips.append((trip_cost, shop))

        cheapest_cost, cheapest_shop = min(trips, key=lambda trip: trip[0])

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
        print(f"{self.name} now has {round(self.money, 2)} dollars")
