class Customer:
    def __init__(self, name: str, product_cart: list, location: list, money: float, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
