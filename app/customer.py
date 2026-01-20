import math

from app.car import Car
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 product_cart: dict,
                 location: list,
                 money: float,
                 car: dict) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = Car(car["brand"], car["fuel_consumption"])
        self.home_location = location[:]

    @staticmethod
    def distance(loc1: list, loc2: list) -> float:
        return math.sqrt((loc1[0] - loc2[0]) ** 2 + (loc1[1] - loc2[1]) ** 2)

    def trip_cost(self, shop: Shop, fuel_price: float) -> float:
        dist = self.distance(self.location, shop.location)
        go_cost = self.car.fuel_cost(dist, fuel_price)
        back_cost = self.car.fuel_cost(dist, fuel_price)
        cart_cost = shop.calculate_cart_cost(self.product_cart)
        return round(go_cost + cart_cost + back_cost, 2)

    def try_shopping(self, shops: list, fuel_price: float) -> None:
        print(f"{self.name} has {self.money} dollars")
        trip_prices = {}
        for shop in shops:
            cost = self.trip_cost(shop, fuel_price)
            trip_prices[shop.name] = cost
            print(f"{self.name}'s trip to the {shop.name} costs {cost}")

        cheapest_shop = min(shops, key=lambda s: trip_prices[s.name])
        cheapest_cost = trip_prices[cheapest_shop.name]

        if self.money >= cheapest_cost and cheapest_cost != float("inf"):
            print(f"{self.name} rides to {cheapest_shop.name}\n")
            self.location = cheapest_shop.location[:]
            cheapest_shop.print_receipt(self.name, self.product_cart)
            print(f"{self.name} rides home")
            self.location = self.home_location[:]
            self.money -= cheapest_cost
            print(f"{self.name} now has {round(self.money, 2)} dollars\n")
        else:
            print(f"{self.name} doesn't have enough money "
                  f"to make a purchase in any shop")
