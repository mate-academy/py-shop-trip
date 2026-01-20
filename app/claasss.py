class Customer:
    def __init__(self, name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car


class Shops:

    def __init__(self, name: str,
                 location: list,
                 products: dict) -> None:
        self.name = name
        self.location = location
        self.products = products
