import datetime
from typing import Any


class Shop:
    def __init__(self, data: dict) -> None:
        self.shop_data = data
        self.name = self.shop_data["name"]
        self.location = self.shop_data["location"]
        self.products = self.shop_data["products"]

    def print_purchase(self,
                       customer: Any,
                       shop_data: tuple[list],
                       list_prod: list
                       ) -> None:
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(
            f"\nDate: {date}\nThanks, {customer.name}, "
            f"for your purchase!\nYou have bought:"
        )
        shop_index = shop_data[1][1]
        total_cost = 0
        best_price = shop_data[0][shop_index]
        for index, product in enumerate(list(
                customer.product_cart.items())
        ):
            s_product = self.products[product[0]]
            product_cost = product[1] * s_product
            total_cost += product_cost
            if (
                    isinstance(product_cost, float)
                    and str(product_cost).split(".")[1] == "0"
            ):
                product_cost = int(product_cost)
            print(f"{product[1]} {list_prod[index]} for "
                  f"{product_cost} dollars")
        print(
            f"Total cost is {total_cost} dollars\nSee you again!\n"
            f"\n{customer.name} rides home\n"
            f"{customer.name} now has{(customer.money - best_price): .2f} "
            f"dollars\n"
        )
