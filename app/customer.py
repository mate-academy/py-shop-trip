from typing import Dict, Listfrom app.car import Carfrom app.shop import Shopclass Customer:    def __init__(            self,            name: str,            product_cart: List,            location: List,            car: Car,            money: int,    ) -> None:        self.name = name        self.product_cart = product_cart        self.location = location        self.car = car        self.money = money        self.total_cost = None    def calculate_trip_cost(self, shop: Dict, fuel_price: float) -> float:        distance_to_shop = self.calculate_distance(shop.location)        fuel_cost = self.car.calculate_trip_cost(distance_to_shop, fuel_price)        shopping_cost = shop.shopping_cost(self.product_cart)        total_cost = fuel_cost + shopping_cost + fuel_cost        return round(total_cost, 2)    def calculate_distance(self, shop_location: List) -> float:        x1, y1 = self.location        x2, y2 = shop_location        distance = ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5        return distance    def calculate_money(self, shop: Shop) -> bool:        shopping_cost = shop.shopping_cost(self.product_cart)        return self.money >= shopping_cost