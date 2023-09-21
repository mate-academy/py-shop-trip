from app.customer import Customer
from app.shop import Shop


class Car:
    def __init__(self, fuel_price: float, other_info: dict) -> None:
        self.fuel_price = fuel_price
        self.brand = other_info["brand"]
        self.fuel_consumption = other_info["fuel_consumption"]

    def count_cost_of_trip(
            self,
            customer: Customer,
            shop: Shop
    ) -> float:

        x1, y1 = customer.location
        x2, y2 = shop.location
        distance_in_km_in_both_sides = (((x1 - x2) ** 2
                                         + (y1 - y2) ** 2) ** 0.5 * 2)
        cost_on_ride_in_2_sides = round(
            (distance_in_km_in_both_sides * self.fuel_consumption / 100)
            * self.fuel_price,
            2
        )

        return cost_on_ride_in_2_sides
