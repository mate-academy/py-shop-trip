from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 wanted_products: dict,
                 location: list[int],
                 money: int,
                 car: dict,
                 ) -> None:
        self.name = name
        self.wanted_products = wanted_products
        self.location = location
        self.money = money
        self.car = Car(car)

    def change_location(self, destination: list) -> None:
        self.location = destination
