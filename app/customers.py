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

    @staticmethod
    def get_data() -> dict:
        with open("app/config.json", "r") as file:
            data = json.load(file)
        return data

    data = get_data()
    fuel_price = data["FUEL_PRICE"]

    shops = []

    for shop_data in data["shops"]:

        shop = Shop(
            shop_data["name"],
            shop_data["location"],
            shop_data["products"]
        )

        shops.append(shop)

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

    def user_go_to_shopping(self) -> None:
        trip_to_outskirts_cost = (
            round(self.count_shop_cost(self.shops[0])
                  + (self.count_fuel(self.shops[0]) * 2), 2))

        trip_to_shop_24_cost = (
            round(self.count_shop_cost(self.shops[1])
                  + (self.count_fuel(self.shops[1]) * 2), 2))

        trip_to_central_shop_cost = (
            round(self.count_shop_cost(self.shops[2])
                  + (self.count_fuel(self.shops[2]) * 2), 2))

        print(f"{self.name} has {self.money} dollars")

        print(f"{self.name}'s trip to the "
              f"{self.shops[0].name} costs {trip_to_outskirts_cost}")

        print(f"{self.name}'s trip to the "
              f"{self.shops[1].name} costs {trip_to_shop_24_cost}")

        print(f"{self.name}'s trip to the "
              f"{self.shops[2].name} costs {trip_to_central_shop_cost}")

        if (self.money > trip_to_central_shop_cost
            or self.money > trip_to_shop_24_cost
           or self.money > trip_to_outskirts_cost):

            if (trip_to_central_shop_cost < trip_to_shop_24_cost
                    and trip_to_central_shop_cost < trip_to_outskirts_cost):
                shop = self.shops[2]

            if (trip_to_shop_24_cost < trip_to_central_shop_cost
               and trip_to_shop_24_cost < trip_to_outskirts_cost):
                shop = self.shops[1]

            if (trip_to_outskirts_cost < trip_to_central_shop_cost
               and trip_to_outskirts_cost < trip_to_shop_24_cost):
                shop = self.shops[0]

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
