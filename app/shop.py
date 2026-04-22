import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: list[int],
        products: dict[str, float],
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, product_cart: dict[str, int]) -> float:
        return sum(
            amount * self.products[product_name]
            for product_name, amount in product_cart.items()
        )

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict[str, int],
    ) -> None:
        print()
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total_cost = 0

        for product_name, amount in product_cart.items():
            product_cost = amount * self.products[product_name]
            total_cost += product_cost
            print(
                f"{amount} {product_name}s for "
                f"{self._format_amount(product_cost)} dollars"
            )

        print(f"Total cost is {self._format_amount(total_cost)} dollars")
        print("See you again!")
        print()

    @staticmethod
    def _format_amount(amount: float) -> str:
        rounded_amount = round(amount, 2)
        if rounded_amount.is_integer():
            return str(int(rounded_amount))

        return str(rounded_amount)
