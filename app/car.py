import dataclasses


@dataclasses.dataclass
class Car:
    fuel_price: float
    fuel_consumption: float
    location_customer: list

    def calculate_trip(self, location_shop: list) -> float:
        distance = ((location_shop[0] - self.location_customer[0]) ** 2
                    + (location_shop[1] - self.location_customer[1]) ** 2)

        cost_trip = (distance ** 0.5 * self.fuel_consumption
                     * self.fuel_price / 100) * 2
        return cost_trip
