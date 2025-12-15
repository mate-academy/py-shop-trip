from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location_h: list,
                 money: int | float,
                 car: Car,
                 ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location_h = location_h
        self.money = money
        self.car = car

    def buy(self, price: float) -> None:
        self.money -= price
