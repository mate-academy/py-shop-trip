import math
from app.shop import Shop


class Car:
    def __init__(
            self, brand: str,
            fuel_consumption: float,
            fuel_price: float,
            product_cart: dict
    ) -> None:
        self.config_path = None
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        self.fuel_price = fuel_price
        self.product_cart = product_cart

    def shop_expenses(self, shop: Shop, customer_location: list) -> float:

        distance_to_shop = self.calculate_distance(
            customer_location[0], customer_location[1],
            shop.location[0], shop.location[1]
        )

        distance_from_shop = self.calculate_distance(
            shop.location[0], shop.location[1],
            customer_location[0], customer_location[1]
        )

        sum_of_distances = distance_to_shop + distance_from_shop
        fuel_needed = sum_of_distances / 100 * self.fuel_consumption

        total_product_price = sum(
            shop.products.get(product, 0) * quantity
            for product, quantity in self.product_cart.items()
        )
        trip_cost = fuel_needed * self.fuel_price + total_product_price
        return round(trip_cost, 2)

    @staticmethod
    def calculate_distance(x1: int, y1: int, x2: int, y2: int) -> float:
        point1 = (x1, y1)
        point2 = (x2, y2)
        distance = math.dist(point1, point2)
        return distance
