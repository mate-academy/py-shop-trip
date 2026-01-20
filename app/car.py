from dataclasses import dataclass


@dataclass
class Car:
    fuel_price: float
    fuel_consumption: float
    customer_loc: list
    shop_loc: list

    def calculate_trip_cost(self) -> float:
        x_loc = (self.customer_loc[0] - self.shop_loc[0]) ** 2
        y_loc = (self.customer_loc[1] - self.shop_loc[1]) ** 2
        distance = (x_loc + y_loc) ** 0.5
        return round(
            (distance / 100) * self.fuel_consumption * self.fuel_price * 2, 2
        )
