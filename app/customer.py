from app.car import Car
from app.shop import Shop
from app.location import calculate_distance


class Customer:
    def __init__(
            self, name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: Car) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_trip_cost(self, distance: float, fuel_price: float) -> float:
        fuel_consumption_per_km = self.car.fuel_consumption / 100
        return distance * fuel_consumption_per_km * fuel_price * 2

    def has_enough_money(self, cost: float) -> bool:
        return self.money >= cost

    def make_purchase(self, shop: Shop, fuel_price: float) -> tuple:
        distance_to_shop = calculate_distance(self.location, shop.location)
        trip_cost = self.calculate_trip_cost(distance_to_shop, fuel_price)
        products_cost = shop.calculate_products_cost(self.product_cart)
        total_cost = trip_cost + products_cost

        if self.has_enough_money(total_cost):
            self.money -= total_cost
            self.location = shop.location
            return True, total_cost, products_cost
        return False, total_cost, products_cost
