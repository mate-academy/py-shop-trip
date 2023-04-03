import math
from app.car import Car


class Customer:
    def __init__(
        self,
        name: str,
        product_cart: dict[str, float],
        money: float,
        car: dict[str, str | float],
        location: list[int],

    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.money = money
        self.car: Car = Car(
            brand=car["brand"],
            fuel_consumption=car["fuel_consumption"]
        )
        self.location = location if location else [0, 0]

    def __repr__(self) -> str:
        return (
            f"{self.name},"
            f" {self.product_cart},"
            f" {self.location},"
            f" {self.money},"
            f" {self.car}"
        )

    def get_fare(
        self, shops: dict, customers: dict, fuel_price: float
    ) -> float:
        total_fare = 0
        for customer in customers:
            for shop in shops:
                distance = math.sqrt(
                    (shop.location[0] - customer.location[0]) ** 2
                    + (shop.location[1] - customer.location[1]) ** 2
                )
                total_fare = \
                    distance * self.car.fuel_consumption / 100 * fuel_price

        return total_fare
