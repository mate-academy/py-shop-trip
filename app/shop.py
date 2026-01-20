from datetime import datetime


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

    def calculate_cart_cost(self, cart: dict) -> float:
        total = 0.0
        for product, qty in cart.items():
            price = self.products.get(product)
            if price is None:
                return float("inf")
            total += price * qty
        return total

    def print_receipt(
            self,
            customer_name: str,
            cart: dict
    ) -> None:
        dt = datetime(2021, 4, 1, 12, 33, 41)
        now = dt.strftime("%m/%d/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, qty in cart.items():
            price = self.products[product] * qty
            total += price
            qty_str = str(int(qty)) if qty == int(qty) else str(qty)
            if price == int(price):
                price_str = str(int(price))
            else:
                price_str = f"{price:.2f}".rstrip("0").rstrip(".")
            print(f"{qty_str} {product}s for {price_str} dollars")
        if total == int(total):
            total_str = str(int(total))
        else:
            total_str = f"{total:.2f}".rstrip("0").rstrip(".")
        print(f"Total cost is {total_str} dollars")
        print("See you again!\n")
