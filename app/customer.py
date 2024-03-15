from app.car import Car


class Customer:
    def __init__(self, name: str, product_cart: dict,
                 location: list, money: float | int, car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)

    def distance(self, shop_location: list[int]) -> float:
        x1, y1 = self.location
        x2, y2 = shop_location
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def spend_money(self, money: float | int) -> None:
        self.money = self.money - money
