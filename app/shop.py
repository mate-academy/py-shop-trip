import datetime

from typing import Tuple


class Shop:
    def __init__(
            self,
            name: str,
            location: Tuple[int, int],
            products: dict
    ) -> None:
        self.__name = name
        self.__location = location
        self.__products = products

    @property
    def name(self) -> str:
        return self.__name

    @property
    def products(self) -> dict:
        return self.__products

    @property
    def location(self) -> list:
        return self.__location

    def buy_products(self, products_to_buy: dict, customer_name: str) -> None:
        total_cost = 0
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(
            f"Thanks, {customer_name}, for your purchase!\n"
            f"You have bought: "
        )
        for product, amount in products_to_buy.items():
            total_price = self.products[product] * amount
            total_cost += total_price
            print(f"{amount} {product}s for {total_price} dollars")
        print(f"Total cost is {total_cost} dollars\nSee you again!\n")
