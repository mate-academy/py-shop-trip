from typing import Dict, List, Union, Any
from app.car import Car
from app.utils import calculate_distance


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: Dict[str, int],
            location: List[Union[int, float]],
            money: Union[int, float],
            car_data: Dict[str, Any]
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car_data["brand"], car_data["fuel_consumption"])
        self.home_location = location

    def calculate_products_cost(self, shop_products: dict) -> float:
        total_cost = 0.0
        for product, quantity in self.product_cart.items():
            if product not in shop_products:
                return None
            total_cost += shop_products[product] * quantity
        return total_cost

    def calculate_trip_cost(
            self,
            shop_location: list,
            shop_products: dict,
            fuel_price: float
    ) -> float:
        if not all(prod in shop_products for prod in self.product_cart):
            return None
        distance = calculate_distance(self.location, shop_location) * 2
        fuel_cost = self.car.fuel_cost(distance, fuel_price)
        products_cost = self.calculate_products_cost(shop_products)
        return round((products_cost + fuel_cost), 2)
