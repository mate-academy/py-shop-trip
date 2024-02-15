import datetime


class Shop:

    def __init__(self, name: str, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products

    def print_purchase(self, customer):
        data = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')
        print(f"\nDate: {data}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        for prod, val in customer.products_card.items():
            print(f"{val} {prod}s for {self.products[prod] * val} dollars")
        print(f"Total cost is {customer.coast_prod_cart(self)} dollars")
        print("See you again!\n")
