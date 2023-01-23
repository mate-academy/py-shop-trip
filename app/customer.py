from dataclasses import dataclass
from typing import List

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    best_shop = None
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def calculate_cost_of_fuel(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        distance = ((self.location[0] - shop.location[0]) ** 2
                    + (self.location[1] - shop.location[1]) ** 2) ** 0.5

        return round(
            (distance / 100 * self.car.fuel_consumption) * fuel_price * 2, 2
        )

    def calculate_cost_of_purchases(
            self,
            shop: Shop
    ) -> float:
        cost_of_purchases = 0
        for key, value in self.product_cart.items():
            cost_of_purchases += (shop.products[key] * value)
        return round(cost_of_purchases, 2)

    def find_the_best_shop(self, shops: List[Shop], fuel_price: float) -> dict:
        print(f"{self.name} has {self.money} dollars")
        shop_info = {}
        for shop in shops:
            total_price = self.calculate_cost_of_purchases(shop) \
                + self.calculate_cost_of_fuel(shop, fuel_price)
            print(f"{self.name}'s trip to the {shop.name} costs {total_price}")
            shop_info[shop.name] = total_price
        best_shop_name = (min(shop_info, key=shop_info.get))
        best_shop_price = shop_info[best_shop_name]
        best_shop = {best_shop_name: best_shop_price}
        for shop in shops:
            if shop.name == best_shop_name:
                best_shop["shop object"] = shop
        self.best_shop = best_shop
        return best_shop

    def customer_check(self, shop: Shop) -> None:
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for key, value in self.product_cart.items():
            print(f"{value} {key}s for {shop.products[key] * value} dollars")
            total_cost += (shop.products[key] * value)
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

    def has_enough_money(self) -> None:
        the_best_shop_name = list(self.best_shop.keys())[0]
        print(f"{self.name} rides to {the_best_shop_name}")
        home_location = self.location
        self.location = self.best_shop["shop object"].location
        print()

        self.customer_check(self.best_shop["shop object"])
        print()

        print(f"{self.name} rides home")
        self.location = home_location

        money_after_shopping = self.money - self.best_shop[the_best_shop_name]
        print(f"{self.name} now has {money_after_shopping} dollars")

    def has_not_enough_money(self) -> None:
        print(f"{self.name} "
              f"doesn't have enough money to make purchase in any shop")
