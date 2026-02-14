from dataclasses import dataclass
from decimal import Decimal
import datetime

from app.customer import Customer


@dataclass
class Shop:
    name: str
    location: list
    products: dict[str, float]

    def customer_purchase(self, customer: Customer) -> None:
        now = datetime.datetime.now()
        print(f"\nDate: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_price = Decimal("0")
        for product, value in customer.product_cart.items():
            price = Decimal(str(value)) * Decimal(str(self.products[product]))
            price = int(price) if price == price.to_integral() else price
            print(f"{value} {product}s for {price} dollars")
            total_price += price
        total_print = (int(total_price)
                       if total_price == total_price.to_integral()
                       else total_price)
        print(f"Total cost is {total_print} dollars\nSee you again!\n")
