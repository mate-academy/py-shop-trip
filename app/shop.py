from __future__ import annotations

import datetime


class Shop:
    shop_list = []

    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products_cost = data["products"]

    def print_datetime(self) -> str:
        return f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        # return "Date: 04/01/2021 12:33:41"

    def count_purchase_price(self, product_cart: dict) -> float:
        total_costs = 0
        for product in product_cart:
            total_costs += (self.products_cost[product]
                            * product_cart[product])

        return total_costs

    @classmethod
    def find_the_cheapest_shop(cls) -> (Shop, float):
        best_shop, best_price = cls.shop_list[0]
        for shop_and_data in cls.shop_list:
            if shop_and_data[1] < best_price:
                best_shop = shop_and_data[0]
                best_price = shop_and_data[1]

        return best_shop, best_price

    def count_price_one_position(
            self, product: str,
            quantity: int
    ) -> float | int:

        return self.products_cost[product] * quantity

    def customer_visit(
            self,
            customer_name: str,
            customer_product_list: dict
    ) -> None:

        total_price_in_shop = 0
        current_datetime = self.print_datetime()
        print(current_datetime)
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")
        for product in customer_product_list:
            quantity = customer_product_list[product]
            price_of_1_position = self.count_price_one_position(
                product,
                quantity
            )

            print(f"{quantity} {product}s for {price_of_1_position} dollars")
            total_price_in_shop += price_of_1_position
        print(f"Total cost is {total_price_in_shop} dollars")
        print("See you again!\n")
