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
        self.coords = location
        self.money = money
        self.car = car

    def fuel_cost(self, fuel_price: float) -> float:
        return self.car["fuel_consumption"] * fuel_price / 100
