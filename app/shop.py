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
        total = 0
        for product, qty in cart.items():
            if product in self.products:
                total += self.products[product] * qty
            else:
                return float("inf")
        return total

    def print_receipt(
            self,
            customer_name: str,
            cart: dict,
            fixed_date: str | None = "04/01/2021 12:33:41"
    ) -> None:
        if fixed_date:
            now = fixed_date
        else:
            now = datetime.now().strftime("%m/%d/%Y %H:%M:%S")
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
