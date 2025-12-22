import datetime

class Shop:

    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products
    
    def calculate_product_cost(self, product_name, quantity):
        if product_name in self.products:
            unit_price = self.products[product_name]
            total_cost = unit_price * quantity
            return total_cost
    
    def print_receipt(self, customer_name, product_cart):
        current_time = datetime.datetime.now().strftime("%m/%d/%Y %H:%M:%S")
        
        print(f"\nDate: {current_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        
        total_cost = 0
        
        for product_name, quantity in product_cart.items():
            cost = self.calculate_product_cost(product_name, quantity)
            total_cost += cost
            print(f"{quantity} {product_name}s for {cost:.2f} dollars")
        
        print(f"Total cost is {total_cost:.2f} dollars")
        print("See you again!\n")
        
        return total_cost