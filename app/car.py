from typing import Any
from math import dist
import datetime


class Calculation:
    def __init__(self, customer: Any, shop: None) -> None:
        self.fuel_price = customer.petrol_today
        self.customer = customer
        self.shop = shop

    def get_distance(self) -> float:
        return dist(self.customer.location, self.shop.location)

    def cost_ride(self) -> float:
        calculation_cost = self.customer.car / 100 * self.get_distance()
        return calculation_cost * self.fuel_price

    def cost_product(self) -> int:
        total_cost = 0
        for product in self.customer.products:
            product_amount = self.customer.products[product]
            showcase = self.shop.product[product]
            total_cost += product_amount * showcase
        return total_cost

    def cost_trip(self) -> float:
        return (self.cost_ride() * 2) + self.cost_product()


class Choose:
    def __init__(self, customer: Any, shops: list) -> None:
        self.customer = customer
        self.shops = shops
        self.markets_list = []

    def list_of_shops(self) -> None:
        for shop in self.shops:
            self.markets_list.append(
                [Calculation(self.customer, shop).cost_trip(),
                 shop.name, shop.product, shop])

    def print_costs(self) -> None:
        print(f"{self.customer.name}"
              f" has {self.customer.money} dollars")

        for info in self.markets_list:
            print(f"{self.customer.name}'s trip"
                  f" to the {info[1]} costs {round(info[0], 2)}")

    def get_best_market(self) -> None:
        self.list_of_shops()
        self.print_costs()
        self.markets_list = sorted(self.markets_list, key=lambda x: x[0])

        if self.customer.money >= self.markets_list[0][0]:
            print(f"{self.customer.name} rides"
                  f" to {self.markets_list[0][1]}\n")
            self.take_check_and_go_home()
        else:
            print(f"{self.customer.name} doesn't have enough money"
                  f" to make purchase in any shop")

    def take_check_and_go_home(self) -> None:
        print(datetime.datetime.now().strftime("Date: %d/%m/20%y %H:%M:%S"))
        print(f"Thanks, {self.customer.name}, for you purchase!")
        print("You have bought: ")

        total_cost = 0
        for product in self.customer.products:
            products = self.markets_list[0][2][product]
            prices = self.customer.products[product]

            total_cost += prices * products

            print(f"{self.customer.products[product]} "
                  f"{product}s for {prices * products} "
                  f"dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        print(f"{self.customer.name} rides home")
        print(f"{self.customer.name} now"
              f" has {round(self.customer.money - self.markets_list[0][0], 2)}"
              f" dollars\n")
