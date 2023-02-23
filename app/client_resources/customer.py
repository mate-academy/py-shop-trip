import os

from datetime import datetime
from typing import List, Dict

import json
from app.shop_resources.shop import Shop
from app.client_resources.Point2D import Point2d


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict[str, int],
            location: Point2d,
            money: float,
            car: object,
            known_shops: List[Shop],
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.known_shops = known_shops
        self.fuel_price = 0
        self._shops_price_and_map = None

    def check_fuel_price(self) -> None:
        file_path = os.path.abspath(os.path.join(os.getcwd(), "config.json"))
        try:
            with open(file_path, "r") as f:
                world_data = json.load(f)
        except FileNotFoundError as fnfe:
            print("World didn't provide data to customer :(")
            raise fnfe

        self.fuel_price = world_data["FUEL_PRICE"]
        del world_data
        print(
            f"{self.name} prayed to God {hash('MateAcademy')} and got "
            f"fuel price for today({self.fuel_price}) dollars "
            f"per km in return!"
        )

    def _count_price_and_map_to_shops(self) -> Dict[Shop, float]:
        self._shops_price_and_map = dict()

        for shop in self.known_shops:
            self._shops_price_and_map[shop] = self._count_price_to_shop(shop)

        return self._shops_price_and_map

    def _count_price_to_shop(self, shop: Shop) -> float:
        __price = self.location.distance_to(shop.location) / 100
        __price *= self.fuel_price * self.car.fuel_consumption
        return __price * 2

    def _count_required_item_prices(self) -> dict[Shop, float]:
        shop_name_overall_price = dict()
        for shop in self.known_shops:
            goods_price = 0
            for good, count in self.product_cart.items():
                goods_price += count * shop.products[good]
            shop_name_overall_price[shop] = goods_price
        return shop_name_overall_price

    def wake_up_and_ride(self) -> None:
        print(f"{self.name} has {self.money} dollars in pocket.")
        self.check_fuel_price()
        shops_and_path = self._count_price_and_map_to_shops()
        shops_and_products_price = self._count_required_item_prices()

        for shop, price in shops_and_products_price.items():
            shops_and_products_price[shop] += shops_and_path[shop]
            print(
                f"{self.name} counted price for travel to {shop.name} "
                f"as {round(shops_and_products_price[shop], 2)}"
            )

        if (min(shops_and_products_price.items(), key=lambda x: x[1])[1]
                > self.money):
            print(f"{self.name} doesn't have enough money "
                  f"to make purchase in any shop :(")
            return

        best_place = min(shops_and_products_price.items(), key=lambda x: x[1])

        self.car.ride_to_location(self, best_place[0].location)
        print(
            f"(Current date: "
            f"{datetime.strftime(datetime.now(), '%Y/%m/%d/, %H:%M:%S')})"
        )
        cheapest_shop = best_place[0]
        cheapest_shop.sell_products(self, self.product_cart)
        print(f"{self.name} is returning home")
        print("." * 36, "-> Home")
        print(f"{self.name} now has {round(self.money, 2)} left.")
