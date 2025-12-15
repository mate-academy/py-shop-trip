import datetime


class Shop:
    def __init__(
        self,
        name: str,
        location: list[float],
        products: dict
    ) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_product_cost(self, cart: dict) -> float:
        total = 0
        for item, quantity in cart.items():
            if item in self.products:
                total += self.products[item] * quantity
        return total

    def print_receipt(
        self,
        customer_name: str,
        cart: dict,
        timestamp: datetime.datetime | None = None
    ) -> float:
        if timestamp is None:
            timestamp = datetime.datetime.now()

        print(f"\nDate: {timestamp.strftime('%Y-%m-%d %H:%M:%S')}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        total = 0
        for item, quantity in cart.items():
            price = self.products[item] * quantity
            print(f"{quantity} {item.lower()}s for {price:.0f} dollars")
            total += price
        print(f"Total cost is {total:.1f} dollars")
        print("See you again!")

        return total
