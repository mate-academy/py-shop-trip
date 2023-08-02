class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def print_purchase_receipt(self, customer, current_time):
        print(f"\nDate: {current_time.strftime('%m/%d/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                product_price = self.products[product]
                total_price = product_price * quantity
                print(f"{quantity} {product}s for {total_price:.2f} dollars")
        print(f"Total cost is {customer.calculate_product_cost(self.products):.2f} dollars")
        print("See you again!")