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

    def __sub__(self, other) -> float:
        return ((self.location[0] - other.location[0]) ** 2 + (self.location[1] - other.location[1]) ** 2) ** 0.5
