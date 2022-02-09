from math import sqrt
from typing import List, Union

from app.car.car import Car
from app.shop.shop import Shop


class Customer:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: List[int],
            money: int,
            car: Car,
    ):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name: str):
        self._name = name

    @property
    def product_cart(self):
        return self._product_cart

    @product_cart.setter
    def product_cart(self, products: dict):
        self._product_cart = products

    @property
    def location(self):
        return self._location

    @location.setter
    def location(self, get_location: list):
        self._location = get_location

    @property
    def money(self):
        return self._money

    @money.setter
    def money(self, money: int):
        self._money = money if money >= 0 else -1

    @property
    def car(self):
        return self._car

    @car.setter
    def car(self, car: Car):
        self._car = car if isinstance(car, Car) else None

    def trip(self, list_shop: List[Shop], fuel_price: Union[int, float]):

        print(f"{self.name} has {self.money} dollars")

        cost_for_shops = {}

        for shop in list_shop:
            cost_products = self.calculate_product(shop)
            cost_ride = self.calculate_ride(shop, fuel_price)
            total_cost = (cost_products[-1] + cost_ride)
            cost_for_shops.update({shop: total_cost})

            print(f"{self.name}'s trip to the {shop.name} costs {total_cost}")

        shop_to_ride = min([cost for cost in cost_for_shops.values()])
        self.money = round(self.money - shop_to_ride, 2)

        if self.money >= 0:
            for shop in cost_for_shops:
                if cost_for_shops[shop] == shop_to_ride:
                    print(f"{self.name} rides to {shop.name}\n")

                    shop.buy_from_customer(self)

                    self.go_home()
                    return
        else:
            print(f"{self.name} doesn't have enough money to make purchase in any shop")
            return

    def calculate_ride(self, shop: Shop, fuel_price: Union[int, float]):
        shop_x = shop.location[0]
        shop_y = shop.location[1]
        home_x = self.location[0]
        home_y = self.location[1]

        destination = round(sqrt(((shop_x - home_x) ** 2) + ((shop_y - home_y) ** 2)), 2)
        destination = round(destination * 100, 3) / 100

        fuel_consumption = round(round(self.car.fuel_consumption * 100, 2) / 10000, 3)
        fuel_price = round(round(fuel_price * 100, 2) / 100, 3)

        litres = round(destination * round(fuel_consumption * fuel_price, 2), 2)
        cost = round(round(litres * 2 * 100, 2) / 100, 2)

        return cost

    def calculate_product(self, shop: Shop):
        total_amount = []
        products = ("milk", "bread", "butter")
        counter = 0
        for product in products:
            cost_for_each = self.product_cart[product] * shop.products[counter].price
            counter += 1
            total_amount.append(cost_for_each)

        amount = sum(total_amount)
        total_amount.append(amount)
        return total_amount

    def go_home(self):
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
