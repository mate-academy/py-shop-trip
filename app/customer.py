from dataclasses import dataclass

from app.shop import Shop
from app.car import Car


@dataclass
class Customer:
    name: str
    product_list: dict
    location: list
    money: int
    car: Car

    def handle_order(self, shop: Shop) -> dict:
        order_cost = 0
        order_info = {}

        for product, value in self.product_list.items():
            order_cost += value * shop.products.get(product)
            order_info[product] = value * shop.products.get(product)

        order_info["total_prod_cost"] = order_cost
        order_info["shop_location"] = shop.location

        return order_info

    def calculate_trip_cost(self,
                            shop: Shop,
                            car: Car,
                            fuel_cost: float) -> float:
        distance = ((self.location[0] - shop.location[0]) ** 2
                    + (self.location[1] - shop.location[1]) ** 2) ** 0.5 * 2
        trip_cost = round(car.fuel_consumption * distance * fuel_cost / 100, 2)

        return trip_cost
