import datetime

from app.customer import Customer


class Shop:
    def __init__(
            self,
            name: str,
            location: list[int],
            products: dict[str, int]
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_check(self, customer: Customer) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0

        for product_name, quantity in customer.product_cart.items():
            products_cost = self.products[product_name] * quantity
            total_cost += products_cost

            if "0" in str(products_cost).split("."):
                products_cost = int(products_cost)

            print(
                f"{quantity} {product_name}s for "
                f"{products_cost} dollars"
            )

        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print()
