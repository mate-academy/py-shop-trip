import dataclasses

from typing import List, Union

from app.car import Car
from app.shop import Shop


@dataclasses.dataclass
class Customers:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def customer_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def product_coast(self, shop: Shop) -> List[int]:
        coast_list = []
        for product, quantity in self.product_cart.items():
            coast_list.append(quantity * shop.products[product])
        return coast_list

    def customer_best_choice(self, shop: Shop, total_cost: float) -> None:
        print(f"{self.name}'s trip to the"
              f" {shop.name} costs {total_cost}")

    def trip_to_the_shop(self, shop: Shop) -> None:
        print(f"{self.name}'s trip to the"
              f" {shop.name} costs")

    def not_enough_money(self) -> None:
        print(f"{self.name} doesn't have enough"
              f" money to make a purchase in any shop")

    def customer_rides_to_shop(self, shop: Shop) -> None:
        print(f"{self.name} rides to {shop.name}\n")

    def customer_rides_home(self, spent_money: Union[int, float]) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has"
              f" {self.money - spent_money} dollars\n")
