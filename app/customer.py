import dataclasses
import math

from app.car import Car
from app.shops import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    def __repr__(self) -> None:
        return self.name

    def get_distance_to_shop(self, shop_location: list) -> float:
        return math.sqrt((shop_location[0] - self.location[0]) ** 2
                         + (shop_location[1] - self.location[1]) ** 2)

    def calculate_road_cost(self, shop: Shop, fuel_price: float) -> float:
        return round(self.get_distance_to_shop(shop.location)
                     * self.car.fuel_consumption / 100 * fuel_price * 2,
                     2)

    def calculate_product_cost(self, shop_price: dict) -> dict:
        total_cost = 0
        product_dict = {}
        for product, count in self.product_cart.items():
            if product in shop_price:
                product_dict[product] = shop_price[product] * count
                total_cost += shop_price[product] * count

        product_dict["total"] = total_cost
        return product_dict
