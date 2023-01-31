import dataclasses


@dataclasses.dataclass
class Car:
    fuel_price: float
    fuel_consumption: float
    location_customer: list[int]

    def calculate_distance(self, location_shop: list[int]) -> float:
        distance = ((location_shop[0] - self.location_customer[0]) ** 2
                    + (location_shop[1] - self.location_customer[1]) ** 2)

        trip_cost = (distance ** 0.5 * self.fuel_consumption
                     * self.fuel_price / 100) * 2

        return trip_cost
