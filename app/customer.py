import math
from .car import Car
from .shop import Shop


class Customer:
    def __init__(self, data: dict) -> None:
        self.name: str = data["name"]
        self.product_cart: dict[str, int] = data["product_cart"]
        self.location: list[int] = data["location"]
        self.money: float = data["money"]
        self.car: Car = Car(
            data["car"]["brand"],
            data["car"]["fuel_consumption"]
        )

    def get_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        """Розраховує повну вартість: дорога туди + продукти + дорога назад."""
        distance = math.sqrt(
            (self.location[0] - shop.location[0]) ** 2
            + (self.location[1] - shop.location[1]) ** 2
        )
        fuel_one_way = ((distance / 100)
                        * self.car.fuel_consumption
                        * fuel_price)
        products_cost = shop.calculate_products_price(self.product_cart)

        return (fuel_one_way * 2) + products_cost

    def drive_to(self, new_location: list[int]) -> None:
        self.location = new_location
