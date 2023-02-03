import datetime
from typing import List

from app.car import Car
from app.shop import Shop

from app.recipe import Recipe


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[int],
            money: float,
            car: Car,
            fuel_price: float
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.fuel_price = fuel_price
        self.__home_location = location

    def get_distance_to_shop(self, location: List[int]) -> float:
        return ((self.location[0] - location[0]) ** 2
                + (self.location[1] - location[1]) ** 2) ** 0.5

    def get_shopping_price(self, shop: Shop) -> Recipe:
        distance_to_shop = self.get_distance_to_shop(shop.location)
        cost_of_trip = self.car.get_cost_of_trip(
            distance_to_shop,
            self.fuel_price
        )
        cost_of_product_cart = shop.get_product_cart_price(self.product_cart)
        if cost_of_product_cart is None:
            return
        return Recipe(
            cost_of_product_cart["recipe"],
            cost_of_trip,
            cost_of_product_cart["price"],
            shop
        )

    def find_trip(self, shops: List[Shop]) -> Recipe:
        trips = [self.get_shopping_price(shop) for shop in shops
                 if self.get_shopping_price(shop) is not None]
        best_buy = min(trips, key=lambda trip: trip.total_price, default=None)
        if best_buy is None:
            return
        if best_buy.total_price > self.money:
            best_buy = None
        for trip in trips:
            print(f"{self.name}'s trip to the "
                  f"{trip.shop.name} costs {trip.total_price}")
        return best_buy

    def go_to_shopping(self, shops: List[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        recipe = self.find_trip(shops)
        if recipe is None:
            print(f"{self.name} doesn't have enough "
                  f"money to make purchase in any shop")
            return
        print(f"{self.name} rides to {recipe.shop.name}")
        self.location = recipe.shop.location
        print()
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        for product in recipe.recipe.keys():
            print(product)
        print(f"Total cost is {recipe.recipe_price} dollars")
        print("See you again!")
        print()
        print(f"{self.name} rides home")
        self.location = self.__home_location
        print(f"{self.name} now has "
              f"{round(self.money - recipe.total_price, 2)} dollars")
        print()
