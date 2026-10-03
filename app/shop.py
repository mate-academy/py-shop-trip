import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_products_cost(self, product_cart: dict) -> float:
        return sum(
            self.products[product] * amount
            for product, amount in product_cart.items()
        )

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict,
    ) -> None:
        total = self.get_products_cost(product_cart)

        print()
        print(
            f"Date: "
            f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}"
        )
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, amount in product_cart.items():
            cost = self.products[product] * amount
            print(
                f"{amount} {product}s for {cost:g} dollars"
            )

        print(f"Total cost is {total:g} dollars")
        print("See you again!")
        print()
