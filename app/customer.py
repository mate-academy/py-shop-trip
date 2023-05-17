from app.shop import Shop


class Customer:
    def __init__(
            self, name: str,
            product_cart: dict,
            location: list,
            money: float,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_products_cost(self, shop: Shop) -> float:
        total = 0
        for product, quantity in self.product_cart.items():
            total += quantity * shop.products.get(product)
        return total
