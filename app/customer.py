from typing import Dict, Tuple, Any
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: Dict[str, int],
                 location: Tuple[int, int], money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Customer":
        car = Car(data["car"]["brand"], data["car"]["fuel_consumption"])
        return cls(
            name=data["name"],
            product_cart=data["product_cart"],
            location=tuple(data["location"]),
            money=data["money"],
            car=car
        )

    def calculate_distance(self, other_location: Tuple[int, int]) -> float:
        x1, y1 = self.location
        x2, y2 = other_location
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def calculate_fuel_cost(self, destination: Tuple[int, int],
                            fuel_price: float) -> float:
        distance = self.calculate_distance(destination)
        return self.car.fuel_cost(distance * 2, fuel_price)

    def calculate_product_cost(self, shop: Shop) -> float:
        return shop.calculate_cart_cost(self.product_cart)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        fuel = self.calculate_fuel_cost(shop.location, fuel_price)
        products = self.calculate_product_cost(shop)
        return round(fuel + products, 2)
