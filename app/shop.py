from dataclasses import dataclass
import datetime
from typing import List, Tuple


@dataclass
class Shop:
    name: str
    location: List[Tuple[float, float]]
    products: dict

    def calculation_of_product_costs(self, product_cart: dict) -> float:
        return sum(
            self.products[product] * quantity
            for product, quantity in product_cart.items()
        )

    def receipt_printing(self, name: str, product_cart: dict) -> None:
        date_now = datetime.datetime.now()
        print(f"Date: {date_now.strftime('%d/%m/%Y %X')}\n"
              f"Thanks, {name}, for your purchase!\n"
              f"You have bought: ")
        for product, quantity in product_cart.items():
            print(f"{quantity} {product}s for "
                  f"{self.products[product] * quantity} dollars")
        print(f"Total cost is "
              f"{self.calculation_of_product_costs(product_cart)} dollars\n"
              f"See you again!\n")
