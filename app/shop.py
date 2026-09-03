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

    def product_cost(
        self,
        product_cart: dict[str, int]
    ) -> float:
        total_cost = 0

        for product_name, quantity in product_cart.items():
            product_price = self.products[product_name]
            total_cost += product_price * quantity

        return total_cost

    def print_receipt(
        self,
        customer_name: str,
        product_cart: dict[str, int],
        purchase_time: datetime.datetime
    ) -> None:
        formatted_time = purchase_time.strftime(
            "Date: %d/%m/%Y %H:%M:%S"
        )

        print(formatted_time)
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product_name, quantity in product_cart.items():
            product_price = self.products[product_name]
            product_total = product_price * quantity

            print(
                f"{quantity} {product_name}s "
                f"for {product_total:g} dollars"
            )

        total_cost = self.product_cost(product_cart)

        print(f"Total cost is {total_cost:g} dollars")
        print("See you again!")
