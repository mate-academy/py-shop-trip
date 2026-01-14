class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def calculate_products_cost(self, cart: dict) -> float:
        total = 0.0
        for item, quantity in cart.items():
            total += self.products[item] * quantity
        return total
