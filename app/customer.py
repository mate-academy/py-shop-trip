from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            products_list: dict,
            location: list,
            money: int,
            car: Car
    ) -> None:
        self.name = name
        self.products_list = products_list
        self.location = location
        self.money = money
        self.car = car

    def calculate_distance(self, location: list) -> float:
        x1, y1 = self.location[0], self.location[1]
        x2, y2 = location[0], location[1]
        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
        return distance

    def calculate_trip_cost(self, shop: Shop, fuel_price: float) -> float:
        distance = self.calculate_distance(shop.location)
        fuel_needed = (distance / 100) * self.car.fuel_consumption
        trip_cost = (2 * fuel_needed * fuel_price) + sum(
            self.products_list[item] * shop.products.get(item, 0)
            for item in self.products_list
        )
        return round(trip_cost, 2)
