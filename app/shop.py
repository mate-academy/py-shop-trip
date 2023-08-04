class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer, purchase_time):
        print(f"\nDate: {purchase_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                product_cost = self.products[product] * quantity
                total_cost += product_cost
                print(f"{quantity} {product}s for {product_cost:.1f} dollars")
        print(f"Total cost is {total_cost:.2f} dollars")
        print("See you again!")

    def remove_products(self, customer):
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                self.products[product] -= quantity