import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict):
        self.name = name
        self.location = location
        self.products = products


    def calculate_products_cost(self, product_cart):
        total = 0
        for product, quantity in product_cart.items():
            if product not in self.products:
                return None
            total += quantity * self.products[product]
        return total

    def print_receipt(self, customer, now=None):
        if now is None:
            now = datetime.datetime.now()
        print(f"\nDate: {now.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print(f"You have bought:")
        total = 0
        for product, quantity in customer.product_cart.items():
            price = self.products[product]
            cost = price * quantity
            total += cost
            print(f"{quantity} {product}s for {cost} dollars")
        print(f"Total cost is {total} dollars")
        print("\nSee you again!")
