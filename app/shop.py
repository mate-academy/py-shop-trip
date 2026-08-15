import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list,
            products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_product_cost(self, product_cart: dict) -> float:
        return sum(
            self.products[product] * amount
            for product, amount in product_cart.items()
        )

    @staticmethod
    def format_cost(cost: float | int) -> float | int:
        if cost == int(cost):
            return int(cost)

        return cost

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict
    ) -> None:
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, amount in product_cart.items():
            total_product_cost = self.products[product] * amount
            product_name = product if amount == 1 else f"{product}s"
            print(
                f"{amount} {product_name} "
                f"for {self.format_cost(total_product_cost)} dollars"
            )

        print(
            f"Total cost is "
            f"{self.format_cost(self.get_product_cost(product_cart))} dollars"
        )
        print("See you again!")
