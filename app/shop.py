from datetime import datetime


class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def calculate_total_cost(self, product_cart):
        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
            else:
                return float('inf')
        return total_cost

    def print_receipt(self, customer_name, product_cart, total_cost):
        print("\nDate:", datetime.now().strftime("%m/%d/%Y %H:%M:%S"))
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in product_cart.items():
            cost = self.products[product] * quantity
            print(f"{quantity} {product}s for {cost:.1f} dollars" if cost % 1 != 0 else f"{quantity} {product}s for {int(cost)} dollars")
        print(f"Total cost is {total_cost:.1f} dollars")
        print("See you again!\n")
