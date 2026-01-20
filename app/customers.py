import datetime
import math

from app.car import Car
from app.shop import Shop


class Customers:
    def __init__(self, customer: dict) -> None:
        self.name = customer["name"]
        self.product_cart = customer["product_cart"]
        self.home_location = customer["location"]
        self.money = customer["money"]
        self.car = Car(customer["car"])
        self.cost_trip = 0
        self.cheap_shop = None
        self.customer_location = customer["location"]

    def customer_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def return_info(self) -> None:
        print(f"{self.name} rides to {self.cheap_shop.name}\n")
        self.customer_location = self.cheap_shop.location
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        total_cost = 0
        for name, count in self.product_cart.items():
            cost = self.cheap_shop.products[name] * self.product_cart[name]
            if int(cost) == cost:
                cost = int(cost)
            else:
                cost = cost
            total_cost += cost
            print(f"{count} {name}s for {cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        print(f"{self.name} rides home")
        self.customer_location = self.home_location
        money_left = round(self.money - self.cost_trip, 2)
        print(f"{self.name} now has {money_left} dollars\n")

    def cheap_trip(self, shops: list[Shop], fuel_price: float) -> None:
        for new_shop in shops:
            fuel_cost = (math.dist(self.home_location, Shop(new_shop).location)
                         * self.car.fuel_consumption / 100 * fuel_price)
            product_cost = sum(Shop(new_shop).products[i]
                               * self.product_cart[i]
                               for i in Shop(new_shop).products)
            trip_cost = round(fuel_cost * 2
                              + product_cost, 2)
            print(f"{self.name}'s trip to the {Shop(new_shop).name}"
                  f" costs {trip_cost}")
            if self.cost_trip > trip_cost or self.cost_trip == 0:
                self.cost_trip = trip_cost
                self.cheap_shop = Shop(new_shop)
        if self.cost_trip > self.money:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
        else:
            self.return_info()
