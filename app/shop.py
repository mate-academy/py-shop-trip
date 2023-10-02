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

    def calculate_price(self, customer: Customer, do_print: bool = False) -> float:
        bill = 0
        for product in customer.product_cart:
            price = self.products[product]
            amount = customer.product_cart[product]
            cost = round(price * amount, 2)
            bill += cost
            if do_print:
                print(f"{amount} {product} for {cost} dollars")
        return bill

    def buy_products(self, customer: Customer) -> float:

        purchase_time = datetime.now().strftime("Date: %m/%d/%Y %H:%M:%S")
        print(f"\n{purchase_time}")
        print(f"Thanks, {customer.name},"
              f" for your purchase!\n You have bought:")
        bill = self.calculate_price(customer, do_print=True)
        print(f"\nTotal cost is {bill} dollars\n See you again!")
        return bill
