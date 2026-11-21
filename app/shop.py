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

    def calculate_products_cost(
        self,
        product_cart: dict[str, int],
    ) -> float:
        return sum(
            quantity * self.products[product]
            for product, quantity in product_cart.items()
        )

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict[str, int],
    ) -> None:
        current_time = datetime.datetime.now()
        products_cost = self.calculate_products_cost(product_cart)

        print(f"Date: {current_time:%d/%m/%Y %H:%M:%S}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in product_cart.items():
            product_cost = quantity * self.products[product]

            print(
                f"{quantity} {product}s for "
                f"{self.format_number(product_cost)} dollars"
            )

        print(
            f"Total cost is "
            f"{self.format_number(products_cost)} dollars"
        )
        print("See you again!")

    @staticmethod
    def format_number(number: float) -> str:
        return f"{number:g}"
