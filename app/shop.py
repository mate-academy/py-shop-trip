from datetime import datetime


class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_products_cost(self, products_cart: dict) -> float:
        total_cost = 0
        for product, quantity in products_cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity

        return total_cost

    def print_receipt(self, customer_name: str, product_cart: dict) -> None:
        now = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"\nDate: {now}")
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for product, quantity in product_cart.items():
            if product in self.products:
                cost = self.products[product] * quantity
                total_cost += cost
                print(f"{quantity} {product}s for {cost} dollars")

        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!\n")
