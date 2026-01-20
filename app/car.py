from decimal import Decimal

from app.location import Location


class Car:
    def __init__(self, brand: str, fuel_consumption: Decimal) -> None:
        self.brand = brand
        self.fuel_consumption = Decimal(str(fuel_consumption))

    def count_fuel_cost(
        self,
        current_location: Location,
        to_location: Location,
        fuel_price: Decimal
    ) -> Decimal:
        distance = current_location.calculate_distance(to_location)

        return (distance * self.fuel_consumption
                * Decimal("0.01") * fuel_price * 2)
