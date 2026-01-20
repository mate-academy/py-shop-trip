from math import sqrt

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int | float,
            car: Car
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.home_location = None

    def calculate_cheapest_option(
            self,
            shops: list[Shop],
            fuel_price: int | float
    ) -> tuple:
        distances = {}

        for shop in shops:
            distance_to_shop = sqrt(
                (shop.location[0] - self.location[0]) ** 2
                + (shop.location[1] - self.location[1]) ** 2
            )
            fuel_cost = (
                (distance_to_shop * 2)
                * self.car.fuel_consumption_for_one_km
                * fuel_price
            )
            products_costs = [
                self.product_cart[product] * shop.products[product]
                for product in self.product_cart
            ]
            overall_cost = round(fuel_cost + sum(products_costs), 2)
            distances[overall_cost] = shop

            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {overall_cost}")

        return min(distances), distances[min(distances)]

    def visit_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location

    def make_a_purchase(
            self, shop: Shop,
            purchase_cost: int | float
    ) -> None:
        self.money -= purchase_cost

        shop.print_check(
            self.name,
            self.product_cart
        )

    def calculate_money(self) -> None:
        print(f"{self.name} now has {self.money} dollars\n")

    def go_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location
        self.calculate_money()
