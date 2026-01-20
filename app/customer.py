from typing import List
from dataclasses import dataclass
from math import sqrt
import datetime

from app.car import Car
from app.shop import Shop


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[int]
    money: int
    car: Car

    def make_purchase(self, shops: List[Shop]) -> None:
        self._print_money_info()
        shop = self._find_cheapest_option(shops)
        if shop:
            print(f"Date: "
                  f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
            print(f"Thanks, {self.name}, for your purchase!\n"
                  "You have bought: ")
            cost = self._calculate_products_cost(shop, show=True)
            print(f"Total cost is {cost} dollars\nSee you again!\n")
            self._ride_home()
        else:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")

    def _print_money_info(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def _ride_home(self) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")

    def _find_cheapest_option(self, shops: List[Shop]) -> Shop | None:
        cheapest_option = shops[0], self._calculate_expenses(shops[0])
        for shop in shops:
            expenses = self._calculate_expenses(shop)
            print(f"{self.name}'s trip to the {shop.name} costs {expenses}")
            if expenses < cheapest_option[1]:
                cheapest_option = shop, expenses
        if cheapest_option[1] > self.money:
            return
        print(f"{self.name} rides to {cheapest_option[0].name}\n")
        self.money -= cheapest_option[1]
        return cheapest_option[0]

    def _calculate_expenses(self, shop: Shop) -> float:
        distance = self._calculate_distance(shop)
        fuel_cost = self._calculate_fuel_cost(distance)
        products_cost = self._calculate_products_cost(shop)
        return round(fuel_cost + products_cost, 2)

    def _calculate_distance(self, shop: Shop) -> int | float:
        return sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )

    def _calculate_fuel_cost(self, distance: float) -> float:
        return self.car.fuel_cons / 100 * distance * Car.fuel_price * 2

    def _calculate_products_cost(
            self,
            shop: Shop,
            show: bool = False
    ) -> float:
        total = 0
        for product, quantity in self.product_cart.items():
            price = quantity * shop.products[product]
            if show:
                print(f"{quantity} {product}s for {price} dollars")
            total += price
        return total
