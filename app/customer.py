import dataclasses
import math
import datetime

from app.car import Car
from app.shop import Shop


@dataclasses.dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int | float
    car: Car

    def _calculate_price_for_road(
            self,
            shop: Shop,
            fuel_price: int | float
    ) -> int | float:
        distance = math.dist(self.location, shop.location)
        fuel_per_one_km = self.car.fuel_consumption / 100
        full_fuel_price = distance * fuel_price * fuel_per_one_km
        return round(full_fuel_price * 2, 2)

    def _calculate_price_for_products(self, shop: Shop) -> int | float:
        price_for_all_products = 0
        for product, price in shop.products.items():
            if product in self.product_cart.keys():
                price_for_all_products += price * self.product_cart[product]
        return price_for_all_products

    def shop_visiting(
            self,
            shops: list[Shop],
            fuel_price: int | float
    ) -> None:
        print(f"{self.name} has {self.money} dollars")
        shops_prices = {}
        for shop in shops:
            road = self._calculate_price_for_road(shop, fuel_price)
            product_price = self._calculate_price_for_products(shop)
            full_price = road + product_price
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {full_price}")
            shops_prices[full_price] = shop

        cheapest_price = min(shops_prices.keys())

        if cheapest_price > self.money:
            print(f"{self.name} doesn't have enough money"
                  f" to make purchase in any shop")
            return

        print(f"{self.name} rides to {shops_prices[cheapest_price].name}\n")
        date = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {date}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for name, number in self.product_cart.items():
            price = shops_prices[cheapest_price].products[name] * number
            total_cost += price
            print(f"{number} {name}s for {price} dollars")

        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - cheapest_price} dollars\n")
