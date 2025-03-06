import dataclasses


@dataclasses.dataclass()
class Car:
    brand: str
    fuel_consumption: float

    def trip_cost(self, distance, fuel_prise):
        return round(self.fuel_consumption / 100
                * distance
                * fuel_prise, 2)


if __name__ == "__main__":
    car = Car("BMW", 9.1)
    print(car.trip_cost(10.154, 5))