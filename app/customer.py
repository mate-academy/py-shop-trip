import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: float,
        car: dict,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location.copy()
        self.money = money
        self.car = Car(
            car["brand"],
            car["fuel_consumption"],
        )

    def get_distance(self, shop: Shop) -> float:
        return math.sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        )

    def get_trip_cost(
        self,
        shop: Shop,
        fuel_price: float,
    ) -> float:
        distance = self.get_distance(shop)

        fuel_cost = self.car.get_fuel_cost(
            distance * 2,
            fuel_price,
        )
        products_cost = shop.get_products_cost(
            self.product_cart
        )

        return fuel_cost + products_cost

    def make_purchase(
        self,
        shop: Shop,
        trip_cost: float,
    ) -> None:
        print(f"{self.name} rides to {shop.name}")

        self.location = shop.location.copy()
        shop.print_receipt(
            self.name,
            self.product_cart,
        )

        print(f"{self.name} rides home")
        self.location = self.home_location.copy()

        self.money -= trip_cost
        print(
            f"{self.name} now has "
            f"{self.money:.2f} dollars"
        )
