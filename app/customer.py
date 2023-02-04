import datetime
from typing import List

from app.car import Car
from app.shop import Shop

from app.bill import Bill


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: List[int],
        money: float,
        car: Car,
        fuel_price: float,
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.fuel_price = fuel_price
        self.__home_location = location

    def get_distance_to_shop(self, location: List[int]) -> float:
        return (
            (self.location[0] - location[0]) ** 2
            + (self.location[1] - location[1]) ** 2
        ) ** 0.5

    def get_shopping_price(self, shop: Shop) -> Bill:
        distance_to_shop = self.get_distance_to_shop(shop.location)
        cost_of_trip = self.car.get_cost_of_trip(
            distance_to_shop, self.fuel_price
        )
        cost_of_product_cart = shop.get_product_cart_price(self.product_cart)
        if cost_of_product_cart is None:
            return
        return Bill(
            cost_of_product_cart["recipe"],
            cost_of_trip,
            cost_of_product_cart["price"],
            shop,
        )

    def find_trip(self, shops: List[Shop]) -> Bill:
        trips = []
        for shop in shops:
            bill = self.get_shopping_price(shop)
            if bill is not None:
                trips.append(bill)
                print(
                    f"{self.name}'s trip to the {bill.shop.name} costs"
                    f" {bill.total_price}"
                )
        best_buy = min(trips, key=lambda trip: trip.total_price, default=None)
        if best_buy is None:
            return
        if best_buy.total_price > self.money:
            best_buy = None
        return best_buy

    def go_to_shopping(self, shops: List[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        recipe = self.find_trip(shops)
        if recipe is None:
            print(
                f"{self.name} doesn't have enough money to make purchase in"
                " any shop"
            )
            return
        print(f"{self.name} rides to {recipe.shop.name}\n")
        self.location = recipe.shop.location
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {self.name}, for you purchase!\n"
            "You have bought: "
        )
        for product in recipe.recipe.keys():
            print(product)
        print(
            f"Total cost is {recipe.recipe_price} dollars\n"
            "See you again!\n\n"
            f"{self.name} rides home"
        )
        self.location = self.__home_location
        print(
            f"{self.name} now has"
            f" {round(self.money - recipe.total_price, 2)} dollars\n"
        )
