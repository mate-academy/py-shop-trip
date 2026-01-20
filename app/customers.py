import datetime
from math import dist
import dataclasses
from app.data_file import fuel_price
from app.shop import Shop
from app.car import Car


@dataclasses.dataclass
class Customer:
    name: str
    location: list[float]
    product_cart: dict
    money: float
    car: Car

    def cost_trip(self, shop: Shop) -> float:
        distance = dist(self.location, shop.location)
        return self.car.fuel_consumption * distance * fuel_price / 100

    def purchases_cost(self, shop: Shop) -> float:
        prise = 0
        for product in self.product_cart.keys():
            prise += self.product_cart[product] * shop.products[product]
        return prise

    def all_trip_cost(self, shop: Shop) -> float:
        price = self.purchases_cost(shop) + 2 * self.cost_trip(shop)
        return price

    def choose_better_cost(self, shops: list[Shop]) -> str | None:
        cost = {shop.name: self.all_trip_cost(shop) for shop in shops}
        for key, value in cost.items():
            if value == min(cost.values()) and value <= self.money:
                return key
        return None

    def make_check(self, shop_name: str, shops: list[Shop]) -> float:
        shop_name = self.choose_better_cost(shops)
        best_shop = self.make_shop(shop_name, shops)
        self.location = best_shop.location
        date_parches = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")

        print(f"Date: {date_parches}\n"
              f"Thanks, {self.name}, for your purchase!\nYou have bought:")
        amount = 0
        for product, value in self.product_cart.items():
            price = value * best_shop.products[product]
            if price % 1 == 0:
                price = int(price)
            print(f"{value} {product}s for {price} dollars")

            amount += round(value * best_shop.products[product], 2)
        return amount

    @staticmethod
    def make_shop(name_shop: str, shops: list[Shop]) -> Shop:
        for shop in shops:
            if name_shop == shop.name:
                return shop
