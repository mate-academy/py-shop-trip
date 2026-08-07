from math import dist

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self, customer_data: dict) -> None:
        self.name = customer_data["name"]
        self.product_cart = customer_data["product_cart"]
        self.home_location = customer_data["location"]
        self.current_location = self.home_location.copy()
        self.money = customer_data["money"]
        self.car = Car(customer_data["car"])

    def calculate_trip_cost(
        self,
        shop: Shop,
        fuel_price: float
    ) -> float:
        total_distance = dist(self.home_location, shop.location) * 2

        fuel_cost = (
            total_distance / 100
            * self.car.fuel_consumption
            * fuel_price
        )

        trip_cost = fuel_cost + shop.calculate_products_cost(self)

        return trip_cost

    def calculate_cheapest_option(
        self,
        shops: list[Shop],
        fuel_price: float
    ) -> tuple[Shop, float]:
        cheapest_cost = None
        cheapest_shop = None
        for shop in shops:
            trip_cost = self.calculate_trip_cost(shop, fuel_price)
            if cheapest_cost is None or trip_cost < cheapest_cost:
                cheapest_cost = trip_cost
                cheapest_shop = shop

        return cheapest_shop, cheapest_cost
