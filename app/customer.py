from app.car import Car
from app.shop import Shop
from dataclasses import dataclass
from typing import Union
from datetime import datetime


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: int
    car: Car

    def make_purchase(self, shop: Shop) -> int | float:
        total_purchase = 0
        for product, price in shop.products.items():
            if product in self.product_cart:
                product_cost = price * self.product_cart[product]
                total_purchase += product_cost
        return total_purchase

    def find_cheapest_shop(
            self,
            shops: list[Shop],
            fuel_price: float
    ) -> Union[Shop, None]:

        min_cost = float("inf")
        cheapest_shop = None
        print(f"{self.name} has {self.money} dollars")

        for shop in shops:
            trip_to_shop = self.car.trip_cost(
                self.location,
                shop.location,
                fuel_price
            )
            total_cost = round(trip_to_shop * 2, 2) + self.make_purchase(shop)
            print(
                f"{self.name}'s trip to the "
                f"{shop.name} costs {round(total_cost, 2)}"
            )

            if total_cost <= min_cost and total_cost <= self.money:
                min_cost = total_cost
                cheapest_shop = shop

        if cheapest_shop:
            print(f"{self.name} rides to {cheapest_shop.name}\n")

            self.make_purchase(cheapest_shop)
            date = (datetime(
                2021, 4, 1, 12, 33, 41
            ).strftime("%m/%d/%Y %H:%M:%S"))
            print(
                f"Date: {date}\n"
                f"Thanks, {self.name}, for your purchase!\n"
                f"You have bought:"
            )
            for product, price in cheapest_shop.products.items():
                total_price = price * self.product_cart[product]
                total_price = (
                    int(total_price) if total_price == int(total_price)
                    else float(total_price)
                )
                print(
                    f"{self.product_cart[product]} "
                    f"{product}s for {total_price} dollars"
                )
            print(
                f"Total cost is "
                f"{self.make_purchase(cheapest_shop)} dollars\n"
                f"See you again!\n\n"
                f"{self.name} rides home"
            )
            self.money -= min_cost
            print(f"{self.name} now has {round(self.money, 2)} dollars\n")

        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        return cheapest_shop
