import json
import math

from app.shop import Shop


class Customer:

    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list[int],
            money: int,
            car: dict
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]

    outskirts_shop = Shop(data["shops"][0]["name"],
                          data["shops"][0]["location"],
                          data["shops"][0]["products"])

    shop_24 = Shop(data["shops"][1]["name"],
                   data["shops"][1]["location"],
                   data["shops"][1]["products"])

    central_shop = Shop(data["shops"][2]["name"],
                        data["shops"][2]["location"],
                        data["shops"][2]["products"])

    def count_shop_cost(self, shop: Shop) -> int:
        counter = 0
        for product in shop.products:
            if product in self.product_cart:
                counter += self.product_cart[product] * shop.products[product]

        return counter

    def count_fuel(self, shop: Shop) -> float:
        fuel = math.sqrt((shop.location[0] - self.location[0]) ** 2
                         + (shop.location[1] - self.location[1]) ** 2)
        fuel *= (self.car["fuel_consumption"] / 100) * self.fuel_price
        return fuel

    def print(self) -> None:
        trip_to_outskirts_cost = (
            round(self.count_shop_cost(self.outskirts_shop)
                  + (self.count_fuel(self.outskirts_shop) * 2), 2))

        trip_to_shop_24_cost = (
            round(self.count_shop_cost(self.shop_24)
                  + (self.count_fuel(self.shop_24) * 2), 2))

        trip_to_central_shop_cost = (
            round(self.count_shop_cost(self.central_shop)
                  + (self.count_fuel(self.central_shop) * 2), 2))

        print(f"{self.name} has {self.money} dollars")

        print(f"{self.name}'s trip to the "
              f"{self.outskirts_shop.name} costs {trip_to_outskirts_cost}")

        print(f"{self.name}'s trip to the "
              f"{self.shop_24.name} costs {trip_to_shop_24_cost}")

        print(f"{self.name}'s trip to the "
              f"{self.central_shop.name} costs {trip_to_central_shop_cost}")

        if self.money > trip_to_central_shop_cost or \
           self.money > trip_to_shop_24_cost or \
           self.money > trip_to_outskirts_cost:

            if trip_to_central_shop_cost < trip_to_shop_24_cost and \
               trip_to_central_shop_cost < trip_to_outskirts_cost:
                shop = self.central_shop

            if trip_to_shop_24_cost < trip_to_central_shop_cost and \
               trip_to_shop_24_cost < trip_to_outskirts_cost:
                shop = self.shop_24

            if trip_to_outskirts_cost < trip_to_central_shop_cost and \
               trip_to_outskirts_cost < trip_to_shop_24_cost:
                shop = self.outskirts_shop

            print(f"{self.name} rides to {shop.name}", end="\n\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {self.name}, for your purchase!")
            print("You have bought: ")

            for product in self.product_cart:
                price = (self.product_cart[product]
                         * shop.products[product])
                if price % 1 == 0:
                    price = int(price)
                print(f"{self.product_cart[product]} "
                      f"{product}s "
                      f"for {price} dollars")

            print(f"Total cost is {self.count_shop_cost(shop)} dollars")
            print("See you again!", end="\n\n")
            print(f"{self.name} rides home")
            money = (self.money - self.count_shop_cost(shop)
                     - round((self.count_fuel(shop) * 2), 2))
            print(f"{self.name} now has "
                  f"{money} "
                  f"dollars", end="\n\n")

        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
