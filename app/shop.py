import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: list,
        products: dict
    ) -> None:
        self.name = name
        self.location = tuple(location)
        self.products = products

    def can_fulfill(self, cart: dict) -> bool:
        return all(product in self.products for product in cart)

    def total_price(self, cart: dict) -> float:
        return sum(self.products[p] * q for p, q in cart.items())

    def print_receipt(self, customer_name: str, cart: dict) -> None:

        print()
        print(f"Date: {datetime.datetime.now():%d/%m/%Y %H:%M:%S}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0
        for product, quantity in cart.items():
            price = self.products[product] * quantity
            total += price
            formatted_price = f"{price:.2f}".rstrip("0").rstrip(".")
            print(f"{quantity} {product}s for {formatted_price} dollars")
        print(f"Total cost is {round(total, 2)} dollars")
        print("See you again!")
        print()
