class Shop:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.location = data["location"]
        self.products = data["products"]

    def has_all_products(self, cart: dict) -> bool:
        return all(product in self.products for product in cart)

    def calculate_cart_total(self, cart: dict) -> float:
        return sum(cart[product] * self.products[product] for product in cart)
