import math
from app.customer import Customer
from app.shop import Shop


class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def cost_per_km(self) -> float:
        return self.fuel_consumption / 100

    def calculate_road_expenses(self, shop: Shop, customer: Customer, fuel_cost: float) -> float:
        distance = math.dist(customer.location, shop.location)
        return distance * self.cost_per_km() * fuel_cost
