from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def total_price_of_products(
        self,
        product_cart: dict,
    ) -> float:
        total = 0.0

        for product, quantity in product_cart.items():
            if product not in self.products:
                return float("inf")

            total += self.products[product] * quantity

        return total

    def buy_products(
        self,
        product_cart: dict,
        customer_name: str,
    ) -> float:
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total = 0.0

        for product, quantity in product_cart.items():
            price = self.products[product] * quantity
            total += price

            print(
                f"{quantity} {product}s for "
                f"{price:g} dollars"
            )

        print(f"Total cost is {total:g} dollars")
        print("See you again!\n")

        return total
