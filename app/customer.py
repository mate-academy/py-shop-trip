import math
from decimal import Decimal

from app.car import Car
from app.shop import Shop


class Customer:
    group_customers: list["Customer"] = []

    def __init__(
        self, **data
    ) -> None:
        self.name = data.get("name")
        self.product_cart = data.get("product_cart")
        self.location = data.get("location")
        self.money = Decimal(data.get("money"))
        self.car = Car(
            data.get("car").get("brand"),
            data.get("car").get("fuel_consumption"))

    def calculate_cost(self, shop: Shop, data: dict) -> Decimal:
        x_coordinate, y_coordinate = self.location
        x1_coordinate, y1_coordinate = shop.location
        distance = Decimal(math.sqrt(
            ((x1_coordinate - x_coordinate) ** 2)
            + ((y1_coordinate - y_coordinate) ** 2)
        ))

        car_cost_there_and_back = (
            (
                (Decimal(self.car.fuel_consumption) * distance) / Decimal(100)
            )
            * Decimal(data["FUEL_PRICE"]) * 2
        )
        products_sum_price = Decimal(0)
        for product, count in self.product_cart.items():
            products_sum_price += Decimal(
                shop.products.get(product, 0)
            ) * count

        return round((car_cost_there_and_back + products_sum_price), 2)

    @classmethod
    def generate_unit(cls, data: dict) -> None:
        for unit in data["customers"]:
            customer = Customer(**unit)
            cls.group_customers.append(customer)


class NotEnoughMoneyException(Exception):
    """Custom exception for cases when customer doesn't have enough money"""
