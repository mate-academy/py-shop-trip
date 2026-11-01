import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_cost(self, product_cart: dict) -> float:
        return sum(
            amount * self.products[product]
            for product, amount in product_cart.items()
        )

    @staticmethod
    def _format_number(value: float) -> float:
        value = round(value, 2)
        return int(value) if value == int(value) else value

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        now = datetime.datetime.now()
        print(f"Date: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, amount in product_cart.items():
            cost = self._format_number(amount * self.products[product])
            print(f"{amount} {product}s for {cost} dollars")
        total = self._format_number(self.products_cost(product_cart))
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
