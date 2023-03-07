from __future__ import annotations

import math
from typing import List

from app.shops import Shop
from app.car import Car


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: int,
                 car: Car) -> None:
        self._name = name
        self._product_cart = product_cart
        self._location = location
        self._money = money
        self._car = car

    def money(self) -> None:
        print(f"{self._name} has {self._money} dollars")

    def customer_in_shop(self, shops: List[Shop]) -> None:
        cheaper_shop = None
        cheaper_shop_cost = None
        for shop in shops:
            price = self._price(shop, self._distance(shop))
            if cheaper_shop_cost and price < cheaper_shop_cost:
                cheaper_shop = shop
                cheaper_shop_cost = price
            elif not cheaper_shop_cost:
                cheaper_shop = shop
                cheaper_shop_cost = price
            print(f"{self._name}'s trip to the {shop.name} costs {price}")
        if self._money < cheaper_shop_cost:
            print(f"{self._name} doesn't have enough"
                  f" money to make purchase in any shop")
        else:
            self._location = shop.location
            print(f"{self._name} rides to {cheaper_shop.name}")
            print()
            cheaper_shop.purchase_receipt(self._name, self._product_cart)
            print()
            print(f"{self._name} rides home\n"
                  f"{self._name} now has "
                  f"{self._money - cheaper_shop_cost} dollars\n")

    def _distance(self, shop: Shop) -> float:
        return math.sqrt((shop.location[0] - self._location[0]) ** 2
                         + (shop.location[1] - self._location[1]) ** 2)

    def _price(self, shop: Shop, distance: float) -> float:
        return round(self._car.fuel_consumption / 100
                     * distance * 2 * 2.4
                     + shop.buy_products(self._product_cart), 2)
