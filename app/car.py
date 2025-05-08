class Car:
    def __init__(self, brand: str,
                 fuel_consumption: float,
                 location: list) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption  # liters per 100 km
        self.location = location  # Uses customer's location

    def cost_for_road(self, distance: float, fuel_price: float) -> float:
        """Calculate the cost of fuel for given distance"""
        return (distance / 100) * self.fuel_consumption * fuel_price
