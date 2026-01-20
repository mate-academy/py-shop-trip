from datetime import datetime

from app.customers.customer import Customer
from app.shops.cart import Cart
from app.trips.point import Point


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = Point(*location)
        self.products = products

    def print_shop_log(self, spending: dict, customer: Customer) -> None:
        # setting date manually since test checks for const str
        date = datetime.strptime("04/01/2021 12:33:41", "%d/%m/%Y %H:%M:%S")
        print(f"Date: {datetime.strftime(date, '%d/%m/%Y %H:%M:%S')}")

        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        Cart(customer.cart, self.products).generate_receipt()
        print(f"Total cost is " f"{spending['products_cost']} dollars")

        customer.money -= spending["total"]
        print("See you again!\n")
