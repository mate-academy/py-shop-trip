from app.car import Car


class Customer:
    customer_list = []

    def __init__(self, name: str, product_card: dict,
                 location: list, money: int, car: Car) -> None:
        self.name = name
        self.product_cart = product_card
        self.location = location
        self.money = money
        self.car = car
        Customer.customer_list.append(self)

    def __str__(self) -> str:
        return f"{self.name} has {self.money} dollars"
