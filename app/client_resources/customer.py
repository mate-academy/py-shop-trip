from dataclasses import dataclass
from typing import List, Dict

from app.shop_resources.shop import Shop
from app.client_resources.Point2D import Point2d


@dataclass
class ServerWithFuelData:
    fuel_price: str


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
        self.fuel_price = ServerWithFuelData.fuel_price

    def _count_price_and_map_to_shops(self) -> Dict[Shop, float]:
        self._shops_price_and_map = dict()

        for shop in self.known_shops:
            self._shops_price_and_map[shop] = self._count_price_to_shop(shop)

        return self._shops_price_and_map

    def _count_price_to_shop(self, shop: Shop) -> float:
        __price = self.location.distance_to(shop.location) / 100
        __price *= self.fuel_price * self.car.fuel_consumption
        return round(__price * 2, 2)

    def _count_required_item_prices(self) -> dict[Shop, float]:
        shop_name_overall_price = dict()
        for shop in self.known_shops:
            goods_price = 0
            for good, count in self.product_cart.items():
                goods_price += count * shop.products[good]
            shop_name_overall_price[shop] = goods_price
        return shop_name_overall_price

    def could_manage_the_ride(
            self,
            shops_and_products_price: dict[Shop, float]
    ) -> bool:
        return (min(shops_and_products_price.items(), key=lambda x: x[1])[1]
                <= self.money)

    def wake_up_and_ride(self) -> None:
        print(f"{self.name} has {self.money} dollars")
        self.check_fuel_price()
        shops_and_path = self._count_price_and_map_to_shops()
        shops_and_products_price = self._count_required_item_prices()

        for shop, price in shops_and_products_price.items():
            shops_and_products_price[shop] += shops_and_path[shop]
            print(
                f"{self.name}'s trip to the {shop.name} "
                f"costs {round(shops_and_products_price[shop], 2)}"
            )

        if not self.could_manage_the_ride(shops_and_products_price):
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")

        else:
            best_place = min(shops_and_products_price.items(),
                             key=lambda x: x[1])

            print(f"{self.name} rides to {best_place[0].name}")
            self.car.ride_to_location(self, best_place[0].location)
            cheapest_shop = best_place[0]
            cheapest_shop.sell_products(self, self.product_cart)
            print(f"{self.name} rides home")
            print(f"{self.name} now has {round(self.money, 2)} dollars")
