class Shop:
    def __init__(self, name: str, location: list[int], products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def print_receipt(self, customer: dict, purchase_time: int) -> None:
        print(f"\nDate: {purchase_time}")
        print(f"Thanks, {customer.name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                product_cost = self.products[product] * quantity
                total_cost += product_cost
                print(f"{quantity} {product}s for {product_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")

    def remove_products(self, customer: dict) -> None:
        for product, quantity in customer.product_cart.items():
            if product in self.products:
                self.products[product] -= quantity
