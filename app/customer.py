from app.shop import Shop


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict,
        location: list,
        money: int,
        car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, shop: Shop) -> float:
        return (
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        ) ** 0.5

    def calculate_products_cost(self, shop: Shop) -> float:
        return sum(
            quantity * shop.products[product]
            for product, quantity in self.product_cart.items()
        )
