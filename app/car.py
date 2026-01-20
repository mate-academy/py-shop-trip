class Car:
    cars = {}

    def __init__(self, name: str, car: dict, fuel_price: float) -> None:
        self.name = name
        self.brand = car["brand"]
        self.fuel_consumption = car["fuel_consumption"]
        self.fuel_price = fuel_price
        self.cars.update({self.name: self})

    def price_for_trip_on_car(self, distance: float) -> float:
        return round(((self.fuel_consumption / 100)
                      * distance * self.fuel_price) * 2, 2)
