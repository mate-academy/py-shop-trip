class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def cost_of_all_products(self, product_cart: dict) -> int:
        cost = 0
        for product, amount in product_cart.items():
            cost += amount * self.products[product]
        return cost
