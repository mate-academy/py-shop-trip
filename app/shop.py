from datetime import datetime

class Shop:
    def __init__(self, name: str, location: tuple, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def generate_purchase_receipt(self, customer_name: str, customer_products: dict, total_cost: float) -> None:
        receipt_time: str = datetime.now().strftime('%m/%d/%Y %H:%M:%S')
        print(f"Date: {receipt_time}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in customer_products.items():
            print(f"{quantity} {product} for {self.products[product] * quantity} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

    def update_product_quantities(self, customer_products: dict) -> None:
        for product, quantity in customer_products.items():
            self.products[product] -= quantity