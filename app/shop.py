import datetime


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

    def calculate_products_cost(self, product_cart: dict) -> float:
        price = 0

        for product, quantity in product_cart.items():
            product_price = self.products[product]
            price += quantity * product_price

        return price

    def print_receipt(self, name: str, product_cart: dict) -> None:
        now = datetime.datetime.now()
        formatted_time = now.strftime("%d/%m/%Y %H:%M:%S")

        print()
        print(f"Date: {formatted_time}")
        print(f"Thanks, {name}, for your purchase!")
        print("You have bought:")

        for product, quantity in product_cart.items():
            product_total = quantity * self.products[product]
            print_value = (
                int(product_total)
                if product_total.is_integer()
                else product_total
            )
            print(f"{quantity} {product}s for {print_value} dollars")

        total_cost = self.calculate_products_cost(product_cart)
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print()
