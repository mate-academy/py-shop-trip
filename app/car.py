from dataclasses import dataclass


@dataclass
class Car:
    brand: str
    fuel_consumption: float

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        total_fuel_lost = distance * self.fuel_consumption / 100
        return total_fuel_lost * fuel_price


if __name__ == "__main__":
    distance = 3.605551275463989
    fuel_price = 2.4
    car = Car("Suzuki", 9.9)
    print(car.calculate_fuel_cost(distance, fuel_price))
