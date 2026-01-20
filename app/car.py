class Car:
    def __init__(self,
                 brand: str,
                 fuel_consumption: float):
        self.brand = brand
        self.fuel_consumption = fuel_consumption


class GasStation:
    def __init__(self, fuel_price: float):
        self.fuel_price = fuel_price

    @property
    def fuel_price(self):
        return self.__fuel_price

    @fuel_price.setter
    def fuel_price(self, fuel_price):
        self.__fuel_price = fuel_price
