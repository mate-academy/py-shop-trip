import dataclasses
from datetime import datetime


@dataclasses.dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def print_check(self,
                    customer_name: str,
                    customer_product_cart: dict
                    ) -> None:
        current_time = datetime(
            2021, 4, 1, 12, 33, 41
        ).strftime("Date: %m/%d/%Y %H:%M:%S")
        print(current_time)
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought: ")
        money_spent = 0
        for product, amount in customer_product_cart.items():
            money_spent += amount * self.products[product]
            plural = "s" if amount > 1 else ""
            print(f"{amount} {product}{plural} "
                  f"for {self.products[product] * amount} dollars")
        print(f"Total cost is {money_spent} dollars")
        print("See you again!\n")
