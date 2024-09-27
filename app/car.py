from math import dist


class Car:
    fuel_price = None

    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def trip_price(self, customer_loc: list, shop_loc: list) -> float:
        distance = dist(customer_loc, shop_loc)
        return ((self.fuel_consumption / 100) * distance) * self.fuel_price * 2

    @staticmethod
    def to_home(name: str, money: int) -> None:
        print(f"{name} rides home")
        print(f"{name} now has {money} dollars\n")
