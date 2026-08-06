
class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def get_cart_cost(self, product_cart: dict) -> int:
        total_cost = 0
        for product, quantity in product_cart.items():
            total_cost += quantity * self.products[product]
        return total_cost
