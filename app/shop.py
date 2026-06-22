from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict[str, float]

    def print_receipt(self, customer_name: str,
                      product_cart: dict[str, int]) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        total_cost = 0

        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, amount in product_cart.items():
            price = self.products[product] * amount
            total_cost += price

            display_price = int(price) if price % 1 == 0 else price
            print(f"{amount} {product}s for {display_price} dollars")

        display_total = int(total_cost) if total_cost % 1 == 0 else total_cost
        print(f"Total cost is {display_total} dollars")
        print("See you again!")
