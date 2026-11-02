import datetime


def format_number(number: float) -> int | float:
    return int(number) if number == int(number) else number


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cart_cost(self, product_cart: dict) -> float:
        return sum(
            quantity * self.products[product]
            for product, quantity in product_cart.items()
        )

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            product_cost = format_number(quantity * self.products[product])
            print(f"{quantity} {product}s for {product_cost} dollars")
        total_cost = format_number(self.cart_cost(product_cart))
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
