import math
from app.car import Car
from app.shop import Shop


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
            brand=car["brand"], fuel_consumption=car["fuel_consumption"]
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

    def get_fare(self, shop: Shop, fuel_price: float) -> float:
        distance = math.sqrt(
            (shop.location[0] - self.location[0]) ** 2
            + (shop.location[1] - self.location[1]) ** 2
        )
        total_fare = distance * self.car.fuel_consumption / 100 * fuel_price
        return total_fare
