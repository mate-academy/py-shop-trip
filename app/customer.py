from datetime import datetime

from app.car import Car
from app.shop import Shop


class Customer:
    customers = []

    def __init__(
        self,
        name: str,
        product_cart: dict[str, int],
        location: list[int, int],
        money: int,
        car: Car,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.current_location = location
        self.home_location = location
        self.money = money
        self.car = car
        self.customers.append(self)
        self.cheapest_shop_trip: Shop | None = None

    def print_amount_of_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def print_not_enough_money(self) -> None:
        print(
            f"{self.name} doesn't have enough money to make "
            "a purchase in any shop"
        )

    def get_purchase_receipt(self, shop_products: dict[str, int]) -> None:
        date = datetime.strptime("04/01/2021 12:33:41", "%m/%d/%Y %H:%M:%S")
        print(
            f"Date: {date.strftime('%m/%d/%Y %H:%M:%S')}",
            f"Thanks, {self.name}, for your purchase!",
            "You have bought:",
            sep="\n",
        )

        for product in self.product_cart.keys():
            amount = self.product_cart[product] * shop_products[product]

            if amount == int(amount):
                amount = int(amount)

            product_name = product if amount <= 1 else product + "s"

            print(
                f"{self.product_cart[product]} {product_name} "
                f"for {amount} dollars"
            )

        print(
            f"Total cost is {self.get_cost_purchase(shop_products)} dollars",
            "See you again!\n",
            sep="\n",
        )

    def find_cheapest_shop_trip(self, shops: list[Shop]) -> None:
        min_cost = float("inf")

        for shop in shops:
            trip_cost = self.calculate_shop_trip(shop)
            print(f"{self.name}'s trip to the {shop.name} costs {trip_cost}")
            if trip_cost < min_cost and self.money - trip_cost >= 0:
                min_cost = trip_cost
                self.cheapest_shop_trip = shop

    def get_cost_purchase(
            self,
            shop_products: dict[str, int | float]
    ) -> int | float:

        return sum(
            self.product_cart[key] * shop_products[key]
            for key in self.product_cart.keys()
        )

    def calculate_shop_trip(self, shop: Shop) -> int | float:
        return round(
            self.car.get_cost_ride_to_shop(
                self.home_location, shop.location
            ) * 2
            + self.get_cost_purchase(shop.products),
            2,
        )

    def ride_to_shop(self) -> None:
        print(f"{self.name} rides to {self.cheapest_shop_trip.name}\n")
        self.current_location = self.cheapest_shop_trip.location

    def ride_to_home_and_check_money(self) -> None:
        check_money = self.money - self.calculate_shop_trip(
            self.cheapest_shop_trip
        )

        print(
            f"{self.name} rides home",
            f"{self.name} now has {check_money} dollars\n",
            sep="\n",
        )
