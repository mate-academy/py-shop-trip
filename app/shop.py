from dataclasses import dataclass
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def calculate_product_cart_cost(self,
                                    product_cart: dict
                                    ) -> int | float:

        cost = 0
        for product, count_product in product_cart.items():
            if product in self.products:
                cost += self.products[product] * count_product
            else:
                print(f"Product {product} is not available in {self.name}")
        return round(cost, 2)

    def generate_receipt(self, customer: "Customer") -> None:

        current_time = datetime(
            2021, 1, 4, 12, 33, 41
        ).strftime("%d/%m/%Y %H:%M:%S")
        total_cost = self.calculate_product_cart_cost(customer.product_cart)

        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        for product, count_product in customer.product_cart.items():
            if product in self.products:
                item_cost = self.products[product] * count_product
                display_cost = int(item_cost) if \
                    (isinstance(item_cost, float)
                     and item_cost.is_integer()) else item_cost

                print(f"{count_product} {product}s for {display_cost} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
