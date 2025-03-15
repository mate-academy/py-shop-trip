class Car:
    def __init__(self, brand: str, fuel_consumption: float) -> None:
        """
        Initialize a Car instance.

        :param brand: The brand of the car.
        :param fuel_consumption: Fuel consumption in liters per 100 kilometers.
        """
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    def calculate_fuel_cost(self, distance: float, fuel_price: float) -> float:
        """
        Calculate the fuel cost for a given distance.

        :param distance: Distance in kilometers.
        :param fuel_price: Price of fuel per liter.
        :return: Total fuel cost in dollars.
        """
        return (self.fuel_consumption / 100) * distance * fuel_price
