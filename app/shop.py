from __future__ import annotations

import datetime


class Shops:

    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def add_shop(shops: list) -> list[Shops]:
        shops_list = []
        for shop in shops:
            new_shop = Shops(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            shops_list.append(new_shop)
        return shops_list

    def cost_of_products(
            self,
            customer_product_cart: dict
    ) -> tuple:
        products_total_cost = 0
        purchase_note = {}

        for product_key in customer_product_cart:
            one_product_total = self.products[product_key] \
                * customer_product_cart[product_key]
            products_total_cost += one_product_total
            purchase_note[product_key] = \
                f"{customer_product_cart[product_key]} " \
                f"{product_key}s for {one_product_total} dollars"
        purchase_note["total"] = products_total_cost
        return purchase_note, products_total_cost

    @staticmethod
    def customer_purchase(
            customer_name: str,
            purchase_note: dict
    ) -> None:
        current_time = datetime.datetime.now()
        print(f"Date: {current_time.strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer_name}, for you purchase!\n"
              f"You have bought: \n"
              f"{purchase_note['milk']}\n"
              f"{purchase_note['bread']}\n"
              f"{purchase_note['butter']}\n"
              f"Total cost is {purchase_note['total']} dollars\n"
              f"See you again!\n")
