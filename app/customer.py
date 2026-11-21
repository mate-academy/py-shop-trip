from math import dist

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
        self.home_location = location.copy()

    def calculate_trip_cost(
        self,
        shop: Shop,
        fuel_price: float,
    ) -> float:
        distance_to_shop = dist(self.location, shop.location)

        one_way_fuel_cost = self.car.calculate_fuel_cost(
            distance_to_shop,
            fuel_price,
        )
        products_cost = shop.calculate_products_cost(
            self.product_cart,
        )

        return one_way_fuel_cost * 2 + products_cost

    def ride_to_shop(self, shop: Shop) -> None:
        self.location = shop.location.copy()
        print(f"{self.name} rides to {shop.name}")

    def ride_home(self) -> None:
        self.location = self.home_location.copy()
        print(f"{self.name} rides home")

    def make_purchase(
        self,
        shop: Shop,
        trip_cost: float,
    ) -> None:
        self.ride_to_shop(shop)

        print()
        shop.print_receipt(self.name, self.product_cart)
        print()

        self.ride_home()
        self.money -= trip_cost

        print(f"{self.name} now has {self.money:.2f} dollars")
