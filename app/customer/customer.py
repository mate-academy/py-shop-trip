from dataclasses import dataclass
from typing import Dict, List

from app.customer.car import Car
from app.shop import Shop
from app.customer.chosen_shop import ChosenShop


@dataclass
class Customer:
    name: str
    home_location: List[int]
    product_cart: Dict[str, int]
    money: int
    car: Car
    location: List[int] = None
    chosen_shop: ChosenShop = None

    def pick_shop(self, shops: List[Shop]) -> None:
        print(f"{self.name} has {self.money} dollars")
        self.chosen_shop = ChosenShop(self.money)
        self.location = self.home_location
        for shop in shops:
            distance_to_shop = (
                (
                    (shop.location[0] - self.location[0]) ** 2
                    + (shop.location[1] - self.location[1]) ** 2
                ) ** 0.5
            )
            one_way_trip_cost = (
                self.car.fuel_consumption * 0.01 * distance_to_shop
                * Car.fuel_price
            )
            shopping_cost = sum(
                self.product_cart[product] * shop.products[product]
                for product in self.product_cart
            )

            total_trip_cost = round(2 * one_way_trip_cost + shopping_cost, 2)

            print(f"{self.name}'s trip to the {shop.name} costs "
                  f"{total_trip_cost}")

            if total_trip_cost <= self.chosen_shop.total_trip_cost:
                self.chosen_shop = ChosenShop(
                    total_trip_cost,
                    shopping_cost,
                    one_way_trip_cost,
                    shop
                )

        if self.chosen_shop.shop:
            print(f"{self.name} rides to {self.chosen_shop.shop.name}\n")
            self.location = self.chosen_shop.shop.location
            self.money -= self.chosen_shop.one_way_trip_cost
        else:
            print(f"{self.name} doesn't have enough money to make a purchase "
                  f"in any shop")

    def ride_home(self) -> None:
        print(f"{self.name} rides home")
        self.location = self.home_location
        self.money = round(self.money - self.chosen_shop.one_way_trip_cost, 2)
        self.chosen_shop = ChosenShop(self.money)
        print(f"{self.name} now has {self.money} dollars\n")
