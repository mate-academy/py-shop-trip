import datetime
from typing import List


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def costing_of_products(self, product_cart: dict) -> float:
        costing = 0
        for name_product, quantity in product_cart.items():
            price = self.products[name_product]
            costing += price * quantity
        return costing

    def receipt(self, product_cart: dict, customer_name: str) -> str:
        date_now = datetime.datetime.now()
        check = (f"Date: {date_now.strftime('%d/%m/%Y %H:%M:%S')}\n"
                 f"Thanks, {customer_name}, for you purchase!\n"
                 "You have bought: \n")

        costing = 0

        for name_product, quantity in product_cart.items():
            price = self.products[name_product]
            costing += price * quantity
            check += (f"{quantity} {name_product}s "
                      f"for {price * quantity} dollars\n")

        check += (f"Total cost is {costing} dollars\n"
                  f"See you again!")
        return check


def creating_shops_classes(shops: List[dict]) -> List[Shop]:
    return [Shop(**shop) for shop in shops]
