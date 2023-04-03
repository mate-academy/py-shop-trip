import math
<<<<<<< HEAD
from app.car import Car
=======


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def __repr__(self) -> str:
        return f"{self.brand}, {self.fuel_consumption}"
>>>>>>> fdd224fdc68e73fd0dc447ddb5a6bcbbf20eca65


class Customer:
    def __init__(
<<<<<<< HEAD
        self,
        name: str,
        product_cart: dict[str, float],
        money: float,
        car: dict[str, str | float],
        location: list[int],
=======
            self,
            name: str,
            product_cart: dict[dict],
            money: int,
            car: dict,
            location: list,
>>>>>>> fdd224fdc68e73fd0dc447ddb5a6bcbbf20eca65
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
<<<<<<< HEAD
            for shop in shops:
                distance = math.sqrt(
                    (shop.location[0] - customer.location[0]) ** 2
                    + (shop.location[1] - customer.location[1]) ** 2
                )
                total_fare = \
                    distance * self.car.fuel_consumption / 100 * fuel_price
=======
            distance = math.sqrt(
                (self.location[0] - customer.location[0]) ** 2
                + (self.location[1] - customer.location[1]) ** 2
            )
            total_fare = (
                    distance * self.car.fuel_consumption
                    / 100 * fuel_price
            )
>>>>>>> fdd224fdc68e73fd0dc447ddb5a6bcbbf20eca65
        return total_fare
