from typing import Dict, Tuple, Any
from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, name: str, product_cart: Dict[str, int],
                 location: Tuple[int, int],
                 money: float, car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> "Customer":
        car_data = data.get("car", {})
        car = Car(brand=car_data.get("brand", "Unknown"),
                  fuel_consumption=car_data.get("fuel_consumption", 0.0))
        return cls(
            name=data.get("name", "Unnamed"),
            product_cart=data.get("product_cart", {}),
            location=tuple(data.get("location", (0, 0))),
            money=data.get("money", 0.0),
            car=car
        )

    def calculate_distance(
            self, other_location: Tuple[int, int]
    ) -> float:
        x1, y1 = self.location
        x2, y2 = other_location
        return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

    def calculate_fuel_cost(
            self, destination: Tuple[int, int], fuel_price: float
    ) -> float:
        distance = self.calculate_distance(destination) * 2  # round trip
        return round(self.car.fuel_cost(distance, fuel_price), 2)

    def calculate_product_cost(self, shop: Shop) -> float:
        total = 0.0
        for product, quantity in self.product_cart.items():
            if product in shop.products:
                total += shop.products[product] * quantity
            else:
                raise ValueError(f"{shop.name} does not sell '{product}'")
        return round(total, 2)

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        fuel = self.calculate_fuel_cost(shop.location, fuel_price)
        products = self.calculate_product_cost(shop)
        return round(fuel + products, 2)
