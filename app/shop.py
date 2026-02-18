import datetime
from dataclasses import dataclass, field

from app.customer import Customer
from app.utils import fmt_money


@dataclass
class Shop:
    name: str
    location: list[int] = field(default_factory=list)
    products: dict[str, float] = field(default_factory=dict)

    def can_sell(self, cart: dict[str, int]) -> bool:
        return all(
            product_name in self.products
            for product_name in cart
        )

    def cart_cost(self, cart: dict[str, int]) -> float:
        return round(
            sum(
                self.products[name] * amount
                for name, amount in cart.items()
            ),
            2
        )

    def print_receipt(self, customer: Customer) -> None:
        date_time_marker = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        print(f"Date: {date_time_marker}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")

        total = 0.0
        for name, amount in customer.product_cart.items():
            line_sum = round(self.products[name] * amount, 2)
            total = round(total + line_sum, 2)
            print(
                f"{amount} {name}s for "
                f"{fmt_money(line_sum)} dollars"
            )

        print(f"Total cost is {fmt_money(total)} dollars")
        print("See you again!")
