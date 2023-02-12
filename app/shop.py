import datetime
TIME_FORMAT = "%d/%m/%Y %H:%M:%S"


class Shop:
    def __init__(self, name: str, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer):
        timestamp = datetime.datetime.now().strftime(TIME_FORMAT)
        total_cost = 0

        print(f"Date: {timestamp}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        for product, amount in customer.product_cart.items():
            item_cost = self.products[product] * amount
            total_cost += item_cost
            print(f"{amount} {product}s for {item_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
