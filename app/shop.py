class Shop:
    def __init__(self, name: str, location: list, products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products

    def __str__(self) -> str:
        return f"{self.name}"

    def calculate_cart_price(self, products_cart: dict) -> float:
        cart_price = 0
        for product, quantity in products_cart.items():
            cart_price += self.products[product] * quantity
        return cart_price
