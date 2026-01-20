from app.car import Car
from math import sqrt


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: float,
            car_name: str,
            car_volume: float
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car_name, car_volume)

    def calculate_distance_to_shop(self, shop: list[int]) -> float:
        x_dot = self.location[0] - shop[0]
        y_dot = self.location[1] - shop[1]
        return round(sqrt(x_dot ** 2 + y_dot ** 2), 2)

    def price_to_get_to_shop(
            self,
            fuel_price: float,
            shop: list[int]
    ) -> float:
        return round(self.car.price_for_km(fuel_price)
                     * self.calculate_distance_to_shop(shop), 2)
