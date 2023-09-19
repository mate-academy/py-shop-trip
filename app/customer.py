import dataclasses
import datetime
import math

from typing import List, Dict, Union

from app.car import Car
from app.shop import Shop


@dataclasses.dataclass
class Customers:
    name: str
    product_cart: Dict[str, int]
    location: list[int]
    money: int
    car: Car

    def customer_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def product_coast(self, shop: Shop) -> List[int]:
        return [
            (quantity * shop.products[product])
            for product, quantity in self.product_cart.items()
        ]

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

    def trip_cost(
            self,
            shop: Shop,
            car: Car,
            fuel_price: float
    ) -> Union[int, float]:

        distance = math.sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )

        total_trip_cost = round(
            (((distance / 100)
              * car.fuel_consumption
              * fuel_price) * 2), 2
        )

        return total_trip_cost

    def customer_check(
            self,
            milks_coast: Union[int, float],
            breads_coast: Union[int, float],
            butters: Union[int, float],
            buy_coast: Union[int, float]
    ) -> None:
        dt = datetime.datetime.now()
        buy_date = dt.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {buy_date}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")
        print(f"{self.product_cart['milk']}"
              f" milks for {milks_coast} dollars")
        print(f"{self.product_cart['bread']}"
              f" breads for {breads_coast} dollars")
        print(f"{self.product_cart['butter']}"
              f" butters for {butters} dollars")
        print(f"Total cost is {buy_coast} dollars")
        print("See you again!\n")
