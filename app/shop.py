import datetime


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, float]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_products_cost(self, product_cart: dict[str, int]) -> float:
        total_cost = 0
        for product, quantity in product_cart.items():
            total_cost += self.products[product] * quantity
        return total_cost

    def print_receipt(
            self, customer_name: str, product_cart: dict[str, int]
    ) -> float:
        total_cost = self.get_products_cost(product_cart)

        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in product_cart.items():

            price = self.products[product] * quantity
            price_str = f"{price:.2f}".rstrip("0").rstrip(".")
            print(f"{quantity} {product}s for {price_str} dollars")

        total_cost_str = f"{total_cost:.2f}".rstrip("0").rstrip(".")
        print(f"Total cost is {total_cost_str} dollars")
        print("See you again!")

        return total_cost
