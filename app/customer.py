from typing import List, Dict
from app.car import Car
from app.shop import Shop
from app.utils import calculate_distance


class Customer:

    def __init__(
            self,
            name: str,
            location: List[float],
            money: float,
            product_cart: Dict[str, int],
            car_data: Dict
    ) -> None:
        self.home_location = list(location)
        self.name = name
        self.location = location
        self.money = money
        self.product_cart = product_cart
        self.car_data = Car(
            brand=car_data["brand"],
            fuel_consumption=car_data["fuel_consumption"]
        )

    def calculate_trip_cost(
            self,
            shop: Shop,
            fuel_price: float
    ) -> float | None:
        distance_to_shop = calculate_distance(self.location, shop.location)
        total_distance = 2 * distance_to_shop

        try:
            product_total = shop.calculate_products_cost(self.product_cart)
            fuel_cost = self.car_data.cost_for_distance(
                distance=total_distance,
                fuel_price=fuel_price
            )
            return float(product_total + fuel_cost)
        except ValueError:
            return None

    def make_purchase(
            self,
            shop: Shop,
            trip_cost: float
    ) -> None:

        if self.money >= trip_cost:
            print(f"{self.name} rides to {shop.name}")
            self.money -= trip_cost
            self.location = shop.location
            shop.print_receipt(self.name, self.product_cart)
            print(f"{self.name} rides home")
            self.location = self.home_location
            print(f"{self.name} now has {self.money:.2f} dollars")
            print("")
        else:
            print(
                f"{self.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
