from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.home_location = location.copy()
        self.money = money
        self.car = car

    def can_afford(self, total_cost: float) -> bool:
        return self.money >= total_cost

    def distance_to(self, shop_location: list) -> float:
        dx = shop_location[0] - self.location[0]
        dy = shop_location[1] - self.location[1]
        return (dx * dx + dy * dy) ** 0.5

    def trip_cost_to(self, shop: Shop, fuel_price: float) -> float:
        distance = self.distance_to(shop.location)
        total_cost = self.car.get_fuel_cost(distance * 2, fuel_price) + shop.product_cost(self.product_cart)
        return round(total_cost, 2)
