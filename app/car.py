class Car:
    fuel_price: int | float = 0
    garage_car = []

    def __init__(self, brand: str, fuel_consumption: float | int) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption
        Car.garage_car.append(self)

    @staticmethod
    def calculate_distance(
            start_location: list,
            end_location: list
    ) -> float:
        distance = ((end_location[0] - start_location[0]) ** 2
                    + (end_location[1] - start_location[1]) ** 2) ** 0.5

        return distance

    def calculate_cost_travel(
            self,
            start_location: list,
            end_location: list
    ) -> float:
        distance = self.calculate_distance(start_location, end_location)
        cost_travel = ((distance / 100) * self.fuel_consumption
                       * self.fuel_price)
        return round(cost_travel * 2, 2)

    @staticmethod
    def travel(
            customer_name: str,
            destination: list,
            name_destination: str
    ) -> list:
        print(f"{customer_name} rides to {name_destination}")

        return destination
