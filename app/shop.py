from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_price_products(self, product_cart: dict) -> float:
        total = 0
        for product, quantity in product_cart.items():
            total += self.products[product] * quantity

        return total

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        total = self.calculate_price_products(product_cart)
        print(f"\nDate:"
              f" {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in product_cart.items():
            price = self.products.get(product, 0)
            cost = price * quantity
            cost = int(cost) if cost == int(cost) else cost
            unit = product if quantity == 1 else product + "s"
            print(f"{quantity} {unit} for {cost} dollars")

        print(f"Total cost is {total} dollars")
        print("See you again!\n")
