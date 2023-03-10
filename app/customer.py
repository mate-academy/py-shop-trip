from app.car import Car
from app.shop import Shop
import math


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: float,
            car: Car
    ) -> None:

        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def road_to_shop(self, shop: Shop, fuel_price: float) -> float:
        distance = (math.sqrt((shop.location[0] - self.location[0]) ** 2
                              + (shop.location[1] - self.location[1]) ** 2))
        consumption = (distance / 100) * fuel_price * \
                      (2 * self.car.fuel_consumption)

        price = self.price(shop)

        return round(consumption + price, 2)

    def choose_shop(self, shops: list[Shop], fuel_price: float) -> Shop:
        chosen_shop = shops[0]
        for shop in shops:
            if self.road_to_shop(chosen_shop, fuel_price) > \
                    self.road_to_shop(shop, fuel_price):
                chosen_shop = shop
        return chosen_shop

    def price(self, shop: Shop) -> float:

        return sum(
            shop.products[product] * amount
            for product, amount in self.product_cart.items()
        )
