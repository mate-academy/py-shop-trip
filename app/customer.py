from app import car as client_car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: [int, float],
                 car_brand: str = None,
                 car_fuel_consumption: [int, float] = None) -> None:
        self.name = name
        self.product_cart = product_cart
        self.money = money
        self.location = location
        self.car = client_car.Car(car_brand, car_fuel_consumption)
