class Car:
    def __init__(
            self,
            brand: str,
            fuel_consumption: float | int,
    ) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @classmethod
    def create_car_from_dict(
            cls,
            car_dict: dict
    ) -> Car:
        return Car(
            brand=car_dict["brand"],
            fuel_consumption=car_dict["fuel_consumption"]
        )

    def fuel_cost_for_trip(
        self,
        distance: float | int,
        fuel_price: float | int
    ) -> float | int:
        return (
            round(
                (
                    (distance / 100)
                    * self.fuel_consumption
                    * fuel_price
                ) * 2,
                2
            )
        )
