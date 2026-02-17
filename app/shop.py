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

    def calculate_cost(self, product_cart: dict) -> float:
        total_cost = 0
        for product_name, quantity in product_cart.items():
            price_per_item = self.products[product_name]
            total_cost += price_per_item * quantity
        return total_cost

    def print_receipt(
            self,
            customer_name: str,
            product_cart: dict,
            dt: datetime.datetime = None
    ) -> None:
        if dt is None:
            dt = datetime.datetime

        date_str = dt.strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date_str}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0

        for product, amount in product_cart.items():
            price_per_item = self.products[product]
            item_total = price_per_item * amount
            total_cost += item_total

            print(f"{amount} {product}s for {item_total:.2f} dollars")

        print(f"Total cost is {total_cost:.2f} dollars")
        print("See you again!")
        print()
