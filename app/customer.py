from dataclasses import dataclass
from app.car import Car
from app.shop import Shop
from typing import List, Tuple


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: List[Tuple[float, float]]
    money: int
    car: dict

    def print_amount_of_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def cost_trip_for_the_products(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float:
        car_for_travel = Car(self.car["brand"], self.car["fuel_consumption"])
        cost_trip = car_for_travel.calculation_of_road_costs(
            self.location,
            shop.location,
            fuel_price
        ) + shop.calculation_of_product_costs(self.product_cart)
        print(f"{self.name}'s trip to the {shop.name} costs {cost_trip}")
        return cost_trip
