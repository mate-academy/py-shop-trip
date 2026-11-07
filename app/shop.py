import datetime


def format_cost(cost: float) -> str:
    rounded_cost = round(cost, 2)

    if rounded_cost == int(rounded_cost):
        return str(int(rounded_cost))

    return str(rounded_cost)


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

    def get_cart_cost(self, product_cart: dict[str, int]) -> float:
        return sum(
            quantity * self.products[product]
            for product, quantity in product_cart.items()
        )

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict[str, int],
    ) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"\nDate: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            cost = quantity * self.products[product]
            print(f"{quantity} {product}s for {format_cost(cost)} dollars")
        total_cost = self.get_cart_cost(product_cart)
        print(f"Total cost is {format_cost(total_cost)} dollars")
        print("See you again!\n")
