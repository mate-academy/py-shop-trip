from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 desired_products: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.desired_products = desired_products
        self.location = location
        self.money = money
        self.car = car
        self.needed_money = 0

    def riding_cost(self, distance: float, fuel_price: float) -> float:
        return round(distance * self.car.fuel_consum / 100 * fuel_price * 2, 2)
