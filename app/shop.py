import datetime

from typing import Any
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list[int],
                 products: dict[str, float | int]
                 ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_purchase_receipt(self, customer: Customer) -> None:
        date = datetime.datetime.now()

        print(f"Date: {date.strftime('%d/%m/%Y %H:%M:%S')}\n"
              f"Thanks, {customer.name}, for your purchase!\n"
              f"You have bought:")
        total_cost = 0
        for product, count in customer.product_cart.items():
            product_recipy = product if count == 1 else product + "s"

            products_price = self.products[product] * count

            if products_price.is_integer():
                products_price = int(products_price)

            print(f"{count} {product_recipy} "
                  f"for {products_price} dollars")
            total_cost += self.products[product] * count
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

    @classmethod
    def from_dict(cls, data: dict[str, Any]) -> Shop:
        return cls(**data)
