class Car:
    """
    Represents a customer's car.
    """
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        """
        :param brand: Car brand (e.g., 'Suzuki').
        :param fuel_consumption: Fuel volume consumption per
            100 kilometers (L/100km).
        """
        self.brand = brand
        self.fuel_consumption = fuel_consumption
