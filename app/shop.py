from __future__ import annotations
import datetime
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products_provides: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products_provides = products_provides

    @staticmethod
    def create_shops(shops: dict) -> list[Shop]:
        shops_list = []
        for shop in shops:
            shops_list.append(
                Shop(
                    shop["name"],
                    shop["location"],
                    shop["products"]
                )
            )
        return shops_list

    @staticmethod
    def date_greeting_farewell(func: callable) -> callable:
        def handler(shop: Shop, customer: Customer) -> callable:
            print(
                f"Date: "
                f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
            )
            print(f"Thanks, {customer.name}, for you purchase!")
            func(shop, customer)
            print("See you again!\n")

        return handler

    @date_greeting_farewell
    def sell_products(self, customer: Customer) -> None:
        print("You have bought: ")
        total_cost = 0
        for product in customer.products_to_buy:
            quantity = customer.products_to_buy[product]
            price = self.products_provides[product]
            charge = quantity * price
            total_cost += charge
            customer.money -= charge
            print(f"{quantity} {product}s for {charge} dollars")
        print(f"Total cost is {total_cost} dollars")
