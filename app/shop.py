
class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def get_cart_cost(self, product_cart):
        total_cost = 0
        for product, quantity in product_cart.items():
            total_cost += quantity * self.products[product]
        return total_cost

