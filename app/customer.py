import dataclasses
import math
from app.shop import Shop
from app.unpack_json_file import fuel_price


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: float
    car: dict

    def road_cost(self, shop: Shop) -> float:
        return round((math.dist(self.location, shop.location) * 2)
                     * (self.car["fuel_consumption"] / 100) * fuel_price, 2)

    def shop_total_cost(self, shop: Shop) -> list:
        total_cost_list = []
        for product, count in self.product_cart.items():
            for shop_product, price in shop.products.items():
                if product == shop_product:
                    total_cost_list.append(count * price)
        return total_cost_list
