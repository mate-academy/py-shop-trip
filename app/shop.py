from dataclasses import dataclass
from math import sqrt


@dataclass
class Shop:
    name: str
    location: list
    products: dict

    def calculate_product_price(
            self,
            customer_cart: dict,
            product: str
    ) -> float:
        cost = customer_cart[product] * self.products[product]
        if cost == int(cost):
            cost = int(cost)
        return cost

    def calculate_cart_price(self, customer_cart: dict) -> float:
        return sum(
            self.calculate_product_price(customer_cart, product)
            for product in customer_cart
        )

    def calculate_trip_price(
            self,
            customer_location: list,
            fuel_price: float,
            fuel_consumption: float,
            customer_cart: dict,
    ) -> float:
        total_cart_price = self.calculate_cart_price(customer_cart)

        distance = sqrt(
            (customer_location[0] - self.location[0]) ** 2
            + (customer_location[1] - self.location[1]) ** 2
        )
        road_price = 2 * (distance * fuel_price * (fuel_consumption / 100))
        return round(road_price + total_cart_price, 2)
