from math import dist
from app.customer import Customer
from app.shop import Shop


class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, customer: Customer,
                            shop: Shop,
                            fuel_price: float) -> float:
        distance = dist(customer.location, shop.location)
        return (self.fuel_consumption / 100 * distance * fuel_price) * 2
