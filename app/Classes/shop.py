from dataclasses import dataclass
from datetime import datetime


class Customer:
    pass


@dataclass
class Shop:
    name: str
    location: tuple
    products: dict

    def __hash__(self) -> int:
        return hash(self.name)

    def buy_products(self, customer: Customer) -> float:
        bill = 0
        purchase_time = datetime.now().strftime("Date: %m/%d/%Y %H:%M:%S")
        print(f"\n{purchase_time}")
        print(f"Thanks, {customer.name},"
              f" for your purchase!\n You have bought:")
        for product in customer.product_cart:
            price = self.products[product]
            amount = customer.product_cart[product]
            cost = price * amount
            bill += cost
            print(f"{amount} {product} for {cost}")
        print(f"\nTotal cost is {bill} dollars\n See you again!")
        return bill
