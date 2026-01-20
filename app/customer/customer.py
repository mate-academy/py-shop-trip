from app.customer.car import Car


class Customer:
    def __init__(self, name: str, products: dict,
                 location: list, money: int, car):
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])
