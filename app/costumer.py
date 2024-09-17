class Customer:
    def __init__(self,
                 name: str,
                 location: list,
                 money: int,
                 fuel_consumption: float,
                 product_cart: dict,) -> None:
        self.name = name
        self.location = location
        self.money = money
        self.fuel_consumption = fuel_consumption
        self.product_cart = product_cart
        self.best_shop = {}
