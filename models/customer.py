from typing import List

from models.car import Car
from models.shop import Shop


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(**car)
        self.car.OWNER = self
        self.cost_trip = 0

    def cost_calculation(self, shops: List[Shop], fuel_price: float) -> dict:
        all_calculations: dict = {}
        print(f"{self.name} has {self.money} dollars")
        for shop in shops:
            patrol = self.car.motion_to_point(shop.location, fuel_price)
            check = self._buy_products(shop)
            cost_trip = round(patrol + check["bill"], 2)
            print(f"{self.name}'s trip to the {shop.name} costs {cost_trip}")
            all_calculations[cost_trip] = [shop, check]
        return all_calculations

    def _buy_products(self, shop: Shop) -> dict:
        check = {"bill": 0}
        for product in self.product_cart:
            if product in shop.products:
                cost = shop.products[product] * self.product_cart[product]
                check[product] = cost
                check["bill"] += cost
        return check

    def _get_data_for_store(self) -> tuple:
        return (self.name, self.product_cart)

    def chose_and_visit_store(self, shops: dict) -> None:
        cost = min(shops)

        if cost <= self.money:
            shop, check = shops[cost]
            print(f"{self.name} rides to {shop.name}\n")
            shop.print_a_check(self.name, self.product_cart, check)
            print(f"{self.name} rides home")
            self.money -= cost
            print(f"{self.name} now has {self.money} dollars\n")
            return
        print(f"{self.name} doesn't have enough "
              f"money to make a purchase in any shop")
