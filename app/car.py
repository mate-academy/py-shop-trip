class Car:
    def __init__(self, location: list, fuel_consumption: float) -> None:
        self.x = location[0]
        self.y = location[1]
        self.fuel_consumption = fuel_consumption

    def calculate_price_of_way(self, shop_x, shop_y, fuel_price: float) -> int:
        distance = (abs(shop_x - self.x) + abs(shop_y - self.y)) * 2
        return distance * (self.fuel_consumption / 100) * fuel_price
