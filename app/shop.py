from dataclasses import dataclass
import datetime


@dataclass
class Shop:
    name: str
    location: list[int]
    products: dict

    def cart_cost(self, cart: dict) -> float:
        total = 0
        for key, value in cart.items():
            total += value * self.products[key]
        return round(total, 2)

    @staticmethod
    def _format_price(value: float | int) -> int | float:
        if isinstance(value, float) and value.is_integer():
            return int(value)
        return value

    def print_receipt(self, customer_name: str, cart: dict) -> None:
        current_time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        for product, quantity in cart.items():
            cost = quantity * self.products[product]
            cost = round(cost, 2)
            cost = self._format_price(round(cost, 2))

            print(f"{quantity} {product}s for {cost} dollars")

        total = self._format_price(self.cart_cost(cart))
        if isinstance(total, float) and total.is_integer():
            total = int(total)

        print(f"Total cost is {total} dollars")
        print("See you again!\n")
