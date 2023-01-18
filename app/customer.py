from app.shop import Shop
from app.fuel_price import FuelPrice
from app.car import Car

import datetime


class Customer:
    def __init__(self, data_customer: dict) -> None:
        self.name = data_customer["name"]
        self.products = data_customer["product_cart"]
        self.location = data_customer["location"]
        self.money = data_customer["money"]
        self.car = Car(data_customer["car"])

    def distance_to_shop(self, shop: Shop) -> float:
        distance = ((shop.location[0] - self.location[0]) ** 2
                    + (shop.location[1] - self.location[1]) ** 2) ** 0.5
        return distance

    def cost_trip(self, shop: Shop, data: FuelPrice) -> float:
        cost = (self.distance_to_shop(shop)
                * self.car.fuel_consumption
                * data.fuel_price / 100)
        return cost * 2

    def full_cost(self, shop: Shop, data: FuelPrice) -> float:
        cost_full = self.cost_trip(shop, data)
        for food in self.products:
            cost_full += self.products[food] * shop.product[food]
        return round(cost_full, 2)

    def shopping(self, shop: Shop, data: FuelPrice) -> None:
        print(f"{self.name} rides to {shop.name}\n")

        spend_money = self.full_cost(shop, data)
        self.location = shop.location
        date_of_purchase = datetime.datetime.now().strftime(
            "%d/%m/%Y %H:%M:%S"
        )
        print(f"Date: {date_of_purchase}")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        total_cost = 0
        for food, count in self.products.items():
            sum_prices = self.products[food] * shop.product[food]
            print(f"{count} {food}s for {sum_prices} dollars")
            total_cost += sum_prices
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")

        print(f"{self.name} rides home")
        self.money -= spend_money
        print(f"{self.name} now has {self.money} dollars\n")
