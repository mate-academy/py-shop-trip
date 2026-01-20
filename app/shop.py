import datetime
from dataclasses import dataclass


@dataclass
class Shop:
    name: str
    location: tuple
    products: dict[str, float]

    def has_products(self, cart: dict[str, int]) -> bool:

        available_products = self.products.keys()

        for product_name in cart.keys():
            if product_name not in available_products:
                return False

        return True

    def calc_product_cost(self, product_name: str, quantity: int) -> float:
        price = float(self.products.get(product_name))
        quantity_float = float(quantity)
        return price * quantity_float

    def print_receipt(
            self,
            customer_name: str,
            cart: dict[str, int],
            total_cost: float
    ) -> None:
        now = datetime.datetime.now()
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")

        if not isinstance(cart, dict):
            raise TypeError("cart must be a dict")

        print(f"Date: {formatted_date}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product_name, quantity in cart.items():

            line_cost = self.calc_product_cost(product_name, quantity)
            if line_cost == int(line_cost):
                formatted_line_cost = f"{int(line_cost)}"
            else:
                formatted_line_cost = f"{line_cost:.2f}"

            product_display_name = (
                f"{product_name}s"
                if not product_name.endswith("s")
                else product_name
            )

            print(f"{quantity} {product_display_name}"
                  f" for {formatted_line_cost} dollars")

        formatted_total_cost = f"{total_cost:.2f}"
        print(f"Total cost is {formatted_total_cost} dollars")
        print("See you again!\n")
