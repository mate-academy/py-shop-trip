from datetime import datetime as dt
import math
from dataclasses import dataclass
from app.car import Car
from app.shop import Shops


@dataclass()
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float
    car: Car

    @staticmethod
    def distance_between_points(
            point1: list[int],
            point2: list[int]
    ) -> float:
        x1, y1 = point1
        x2, y2 = point2

        return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

    def get_total_cost_in_shop(self, shop: Shops) -> int:
        total_cost = sum(
            [shop.products[product]
             * self.product_cart[product]
             for product in self.product_cart.keys()]
        )
        return total_cost

    def get_price_for_trip(
            self,
            fuel_price: float,
            shop: Shops
    ) -> float:
        distance = self.distance_between_points(self.location, shop.location)
        spend_money_for_fuel = 2 * distance \
            * (self.car.fuel_for_100_km / 100) * fuel_price
        return spend_money_for_fuel

    def get_receipt(self, shop: Shops) -> None:
        print(f"Date: "
              f"{dt(2021, 1, 4, 12, 33, 41).strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {self.name}, for you purchase!\n"
              "You have bought: ")
        for product in self.product_cart:
            print(f"{self.product_cart[product]} {product}s "
                  f"for "
                  f"{shop.products[product] * self.product_cart[product]}"
                  f" dollars")
        print(f"Total cost is {self.get_total_cost_in_shop(shop)} dollars")
        print("See you again!\n")

    def get_best_option(self, fuel_price: float, shops: list) -> None:
        get_shopping_cost = {}
        array_cost_of_trip = []
        print(f"{self.name} has {self.money} dollars")
        for shop in shops:
            cost_of_trip = round(self.get_total_cost_in_shop(shop)
                                 + self.get_price_for_trip(fuel_price, shop),
                                 2)
            get_shopping_cost[shop.name] = cost_of_trip
            array_cost_of_trip.append(cost_of_trip)
            print(f"{self.name}'s trip to the {shop.name} costs "
                  f"{cost_of_trip}")
        if min(get_shopping_cost.values()) > self.money:
            print(f"{self.name} doesn't have enough money"
                  f" to make purchase in any shop")
            return
        check_shop_name = ""
        for key, value in get_shopping_cost.items():
            if value == min(get_shopping_cost.values()):
                print(f"{self.name} rides to {key}\n")
                check_shop_name = key

        for shop in shops:
            if shop.name == check_shop_name:
                self.get_receipt(shop)
        print(f"{self.name} rides home")
        print(f"{self.name} now has "
              f"{round(self.money - min(get_shopping_cost.values()), 2)} "
              f"dollars\n")
