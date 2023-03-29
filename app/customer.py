from dataclasses import dataclass

import datetime
from math import sqrt

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: object = Car

    def current_balance(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def calculate_distance(self,
                           shop_detail: Shop) -> float:
        distance = ((sqrt((shop_detail.location[0]
                           - self.location[0]) ** 2
                          + (shop_detail.location[1]
                             - self.location[1]) ** 2)))
        return distance

    def calculate_gasoline(self,
                           fuel_price: int,
                           shop_detail: Shop) -> int:
        gasoline = (self.calculate_distance(shop_detail)
                    * (self.car["fuel_consumption"] / 100)
                    * fuel_price)
        return gasoline

    def calculate_product(self, shop_detail: Shop) -> float:
        product = (self.product_cart["milk"]
                   * shop_detail.products["milk"]
                   + self.product_cart["bread"]
                   * shop_detail.products["bread"]
                   + self.product_cart["butter"]
                   * shop_detail.products["butter"])
        return product

    def find_min_cost_shop(self,
                           fuel_price: int,
                           list_of_shop: list) -> dict:
        min_coast_shop = {}
        for shop_detail in list_of_shop:
            total = round(self.calculate_gasoline(fuel_price, shop_detail)
                          * 2 + self.calculate_product(shop_detail), 2)
            print(f"{self.name}'s trip to the "
                  f"{shop_detail.name} costs {total}")
            min_coast_shop[total] = shop_detail.name
        return min_coast_shop

    def final_result(self,
                     fuel_price: int,
                     list_of_shop: list) -> None:
        cheap_shop = self.find_min_cost_shop(fuel_price, list_of_shop)
        if min(cheap_shop.keys()) < self.money:
            print(f"{self.name} rides to "
                  f"{cheap_shop.get(min(cheap_shop.keys()))}\n")
            data = datetime.datetime.now().strftime("%d/%m/20%y %H:%M:%S")
            print(f"Date: {data}")
            print(f"Thanks, {self.name}, for your purchase!")

            for detail in list_of_shop:
                if detail.name == cheap_shop.get(min(cheap_shop.keys())):
                    products = [self.product_cart["milk"]
                                * detail.products["milk"],
                                self.product_cart["bread"]
                                * detail.products["bread"],
                                self.product_cart["butter"]
                                * detail.products["butter"]]
                    add_inf = iter(products)
                    print("You have bought: ")
                    for key, value in self.product_cart.items():
                        print(f"{value} {key}s for {next(add_inf)} dollars")
                    print(f"Total cost is {sum(products)} dollars")
                    print("See you again!\n")
                    print(f"{self.name} rides home")
                    fuel = self.calculate_gasoline(fuel_price, detail)
                    print(f"{self.name} now has "
                          f"{round(self.money - sum(products) - fuel * 2, 2)}"
                          f" dollars\n")
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
