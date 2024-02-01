from math import dist


class Car:
    def __init__(self, fuel_price: float, car_info: dict) -> None:
        self.fuel_price = fuel_price
        self.brand = car_info.get("brand")
        self.fuel_consumption = car_info.get("fuel_consumption")

    def get_fuel_cost(self, home_point: list, shop_point: list) -> float:
        distance = dist(home_point, shop_point)
        fuel_needed = (self.fuel_consumption / 100) * distance
        return round(fuel_needed * self.fuel_price * 2, 2)
