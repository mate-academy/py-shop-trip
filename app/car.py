from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float
    fuel_price: float

    def calculate_cost_of_trip(
            self,
            start_location: list[int],
            finish_location: list[int],
    ) -> float:
        x_coords_distance = (finish_location[0] - start_location[0]) ** 2
        y_coords_distance = (finish_location[-1] - start_location[-1]) ** 2
        distance = (x_coords_distance + y_coords_distance) ** .5

        trip_cost = (self.fuel_consumption
                     / 100.0
                     * distance
                     * self.fuel_price
                     * 2.0)

        return round(trip_cost, 2)
