import datetime
from typing import List

from app.distance import Distance
from app.shop import Shop
from app.action import total_cost_products, min_price, total_cost, list_to_buy


class Customer:
    def __init__(
            self,
            name: str,
            amount_money: float,
            products: dict,
            location: list,
            fuel_consumtion: float | int
    ) -> None:
        self.name = name
        self.car = fuel_consumtion
        self.amount_money = amount_money
        self.products = products
        self.location = location

    def amount_of_money(self) -> None:
        print(f"{self.name} has {self.amount_money} dollars")

    def check_price(
            self,
            shops: [Shop],
            distance: Distance,
            full_price: int | float
    ) -> None:
        for shop in shops:
            price_for_trip = total_cost(self, shop, distance, full_price)
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {price_for_trip}")

    def shopping(
            self,
            shops: List[Shop],
            distance: Distance,
            full_price: int | float
    ) -> None:
        for shop in shops:
            if shop.name == min_price(self, shops, distance, full_price):
                if total_cost_products(self, shop) < self.amount_money:
                    cheapest_shop = min_price(
                        self, shops, distance, full_price
                    )
                    print(
                        f"{self.name} rides to {cheapest_shop}\n"
                    )
                    data = datetime.datetime.now().strftime(
                        "%d/%m/%Y %H:%M:%S"
                    )
                    print(f"Date: {data}")
                    print(f"Thanks, {self.name}, for your purchase!")
                    print("You have bought: ")
                    for product, quantity in self.products.items():
                        list_to_buy(product, quantity, shop.products[product])
                    price = total_cost_products(self, shop)
                    print(f"Total cost is {price} dollars")
                    print("See you again!\n")
                    print(f"{self.name} rides home")
                    amount = self.amount_money - total_cost(
                        self, shop, distance, full_price
                    )
                    print(f"{self.name} now has {amount} dollars\n")
                else:
                    print(
                        f"{self.name} doesn't have enough money"
                        f" to make purchase in any shop"
                    )
