import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: list[float],
        products: dict,
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def products_cost(
        self,
        cart: dict,
    ) -> float:
        total = 0.0

        for product, amount in cart.items():
            total += self.products[product] * amount

        return total

    def print_receipt(
        self,
        customer_name: str,
        cart: dict,
    ) -> float:
        total = 0.0

        print()
        print(
            "Date:",
            datetime.datetime.now().strftime(
                "%d/%m/%Y %H:%M:%S"
            ),
        )
        print(
            f"Thanks, {customer_name}, for your purchase!"
        )
        print("You have bought:")

        for product, amount in cart.items():
            cost = self.products[product] * amount
            total += cost

            print(
                f"{amount} {product}s "
                f"for {cost} dollars"
            )

        print(
            f"Total cost is {total} dollars"
        )
        print("See you again!")
        print()

        return total
