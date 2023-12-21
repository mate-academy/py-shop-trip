class Car:
    def __init__(self, brand: str, fuel_consumption: int | float) -> None:
        self.brand = brand
        self.fuel_consumption = fuel_consumption

    @staticmethod
    def calculate_distance(point1: list, point2: list) -> float:
        x1, y1 = point1
        x2, y2 = point2
        result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        return result

    def road_cost(self, distance: float, fuel_price: float) -> float:
        fuel_consumption = self.fuel_consumption
        price_for_one_km = fuel_consumption / 100 * fuel_price
        road_cost = round(distance * 2 * price_for_one_km, 2)

        return road_cost
