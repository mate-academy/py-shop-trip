import datetime
from app.customers import Customer


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_check(self, customer: Customer) -> None:
        home, customer.location = customer.location, self.location
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        amount = 0
        for product in customer.product_cart:
            quantity = customer.product_cart[product]
            price = quantity * self.products.get(product, 0)
            print(f"{quantity} {product}s for {price} dollars")
            amount += price
        print(f"Total cost is {amount} dollars")
        print("See you again!\n")
        customer.location = home
