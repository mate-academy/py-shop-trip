from datetime import datetime

from app.customer import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, product_cart: dict) -> float:
        total_price = 0
        for product in product_cart:
            total_price += product_cart[product] * self.products[product]
        return total_price

    def print_receipt(self, customer: Customer) -> None:
        print("Date:", datetime(
            2021,
            1,
            4,
            12,
            33,
            41
        ).strftime("%d/%m/%Y %H:%M:%S"))
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, count in customer.products_to_buy.items():
            price = round(self.products[product] * count, 2)
            if isinstance(price, float) and price.is_integer():
                formatted_price = int(price)
            else:
                formatted_price = price

            if count > 1:
                print(f"{count} {product}s for {formatted_price} dollars")
            elif count == 1:
                print(f"{count} {product} for {formatted_price} dollars")

        print(f"Total cost is "
              f"{self.calculate_product_cost(customer.products_to_buy)} "
              f"dollars")
        print("See you again!\n")
