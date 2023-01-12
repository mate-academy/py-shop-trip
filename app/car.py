from math import sqrt
from app.customer import Customer
from app.shop import Shop


class Car:
    def __init__(self, brand: str, fuel_consumption: int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def car_expenses(
            self,
            fuel_price: float,
            customer: Customer,
            shop: Shop
    ) -> float:
        distance = 0

        for i in range(len(customer.location)):
            distance += (shop.location[i] - customer.location[i]) ** 2

        consumption = (
            round(
                fuel_price * self.fuel_consumption * sqrt(distance) * 2 / 100,
                2
            )
        )
        return consumption
