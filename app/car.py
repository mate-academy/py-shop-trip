class Car:
    def __init__(self,
                 brand: str,
                 location: list,
                 fuel_price: int,
                 fuel_consumption: int) -> None:
        self.brand = brand
        self.location = location
        self.fuel_price = fuel_price
        self.fuel_consumption = fuel_consumption

    def calculate_distance(self, point2: list) -> float:
        x1, y1 = self.location
        x2, y2 = point2
        result = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5

        return result

    def road_cost(self, distance: float) -> float:
        price_for_one_km = self.fuel_consumption / 100 * self.fuel_price
        road_cost = round(distance * 2 * price_for_one_km, 2)

        return road_cost
