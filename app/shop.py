class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def calculate_cart_cost(self, cart: dict) -> float:
        total_cost = 0
        for product, quantity in cart.items():
            if product in self.products:
                total_cost += self.products[product] * quantity
            else:
                return None
        return total_cost

    def print_receipt(self, customer_name: str, cart: dict,
                      total_cost: float) -> None:
        print(f"Thanks, {customer_name}, for your purchase!")
        print("You have bought:")
        for product, quantity in cart.items():
            total_product_price = self.products[product] * quantity
            if total_product_price == int(total_product_price):
                print(f"{quantity} {product}s for"
                      f" {int(total_product_price)} dollars")
            else:
                print(f"{quantity} {product}s for"
                      f" {total_product_price} dollars")
        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!\n")
