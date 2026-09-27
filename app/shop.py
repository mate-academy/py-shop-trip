import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: list[int | float],
        products: dict[str, int | float],
    ) -> None:
        self.name = name
        self.location = location.copy()
        self.products = products

    def calculate_cart_cost(
        self,
        product_cart: dict[str, int | float]
    ) -> float:
        total = 0.0
        for name, quantity in product_cart.items():
            price = self.products[name]
            total += quantity * price
        return total

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict[str, int | float],
    ) -> None:
        current_time = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        total_cost = self.calculate_cart_cost(product_cart)

        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for name, quantity in product_cart.items():
            product_cost = round(quantity * self.products[name], 2)

            print(
                f"{quantity} {name}s for "
                f"{product_cost:g} dollars"
            )

        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!")
