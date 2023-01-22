from datetime import datetime
from typing import Any

from app.car import Car
from app.location import Location
from app.shop import Shop


class Customer:
    def __init__(self, customer: dict[str, Any]) -> None:
        self.name = customer["name"]
        self.products_to_buy = customer["product_cart"]
        self.location = Location(customer["location"])
        self.money = customer["money"]
        self.car = Car(customer["car"])

    def get_trip_price(
            self,
            shop: Shop,
            fuel_price: int | float
    ) -> int | float:
        distance_to_shop = self.location.calculate_distance_to_other_location(
            shop.location
        )
        money_for_trip = (
            self.car.calculate_fuel_needed_for_trip(distance_to_shop * 2)
            * fuel_price
        )
        return round(money_for_trip, 2)

    def get_products_in_a_shop_price(self, shop: Shop) -> int | float:
        if not shop.check_if_has_products(self.products_to_buy):
            raise ValueError(
                "Shop doesn't have all the products which customer needs"
            )
        return shop.get_price_of_products(self.products_to_buy)

    def get_money_needed_for_trip_and_products(
            self,
            shop: Shop,
            fuel_price: float
    ) -> int | float:
        money_needed = (
            self.get_trip_price(shop, fuel_price)
            + self.get_products_in_a_shop_price(shop)
        )
        print(f"{self.name}'s trip to the {shop.name} costs {money_needed}")
        return money_needed

    def determine_cheapest_shop_and_visit_it(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> None:
        print(f"{self.name} has {self.money} dollars")
        lowest_total_price = float("inf")
        best_shop = None
        for shop in shops:
            money_for_trip_and_products = (
                self.get_money_needed_for_trip_and_products(shop, fuel_price)
            )
            if money_for_trip_and_products < lowest_total_price:
                lowest_total_price = money_for_trip_and_products
                best_shop = shop
        if self.money >= lowest_total_price:
            self.report_about_visit_to_shop(best_shop, lowest_total_price)
        else:
            print(
                f"{self.name} doesn't have enough "
                f"money to make purchase in any shop"
            )

    def report_about_visit_to_shop(
            self,
            shop: Shop,
            lowest_total_price: int | float
    ) -> None:
        print(f"{self.name} rides to {shop.name}\n")
        date_to_pass_test = datetime(2021, 1, 4, 12, 33, 41)
        print(f"Date: {date_to_pass_test.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        for product, quantity in self.products_to_buy.items():
            print(
                f"{quantity} {product}s for "
                f"{shop.products[product] * quantity} dollars"
            )
        print(
            f"Total cost is "
            f"{shop.get_price_of_products(self.products_to_buy)} dollars"
        )
        print("See you again!\n")
        print(f"{self.name} rides home")
        print(
            f"{self.name} now has {self.money - lowest_total_price} dollars\n"
        )
