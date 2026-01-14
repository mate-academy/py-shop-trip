import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, product_cart: dict) -> float:
        return sum(
            self.products[product] * qty
            for product, qty in product_cart.items()
        )

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:

        now = (datetime.datetime.now())
        date_str = now.strftime("%d/%m/%Y %H:%M:%S")
        total = self.calculate_product_cost(product_cart)

        print(f"\nDate: {date_str}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, qty in product_cart.items():
            cost = self.products[product] * qty
            cost = (
                int(cost)
                if isinstance(cost, float) and cost.is_integer()
                else cost
            )
            print(f"{qty} {product}s for {cost} dollars")
        total = int(total) if total.is_integer() else total
        print(f"Total cost is {total} dollars")
        print("See you again!\n")
