from app.car import Car
from typing import Dict, Any, List
from app.shop import Shop


class Customer:
    def __init__(self, info: Dict[str, Any], fuel_price: float) -> None:
        self.name = info["name"]
        self.product_cart = info["product_cart"]
        self.location = info["location"]
        self.money = info["money"]
        self.car = Car(info["car"], fuel_price)

    def calculate_trip_cost(self, destination: List[float]) -> float:
        return self.car.calculate_trip_cost(self.location, destination)

    def go_to_shop(self, shop: Shop) -> None:
        trip_cost = self.calculate_trip_cost(shop.location)
        print(f"{self.name} rides to {shop.name}")

        if self.money >= trip_cost:
            self.money -= trip_cost
            self.location = shop.location
            shop.sell_products(self)

    def go_home(self) -> None:
        print(f"{self.name} rides home")
