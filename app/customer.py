import dataclasses
import math
from app.shop import Shop
from app.unpack_json_file import unpack


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list[int]
    money: float
    car: dict

    def road_cost(self, shop: Shop) -> float:
        return round((math.dist(self.location, shop.location) * 2)
                     * (self.car["fuel_consumption"] / 100)
                     * unpack("app/config.json", "fuel_price"), 2)

    def shop_total_cost(self, shop: Shop) -> float:
        return sum(
            count * shop.products[product] for product,
            count in self.product_cart.items() if product in shop.products)
