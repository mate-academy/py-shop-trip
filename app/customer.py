import math
from app.shop import Shop


class Customer:
    def __init__(self,
                 name: str,
                 products: dict,
                 location: list,
                 money: int,
                 car: dict):
        self.name = name
        self.products = products
        self.location = location
        self.money = money
        self.car = car

    def calculate_fuel_price(self, shop_location: list, fuel_price: float):
        distance = math.sqrt(
            ((shop_location[0] - self.location[0]) ** 2) /
            + ((shop_location[1] - self.location[1]) ** 2)
        )

        one_km_fuel_consumption = self.car["fuel_consumption"] / 100
        return round(distance * one_km_fuel_consumption * fuel_price * 2, 2)

    def calculate_trip_price(self, shop: Shop, fuel_price: float):
        total = self.calculate_fuel_price(shop.location, fuel_price)
        for product in self.products.items():
            total += shop.calculate_prices(product[0], product[1])
        return total

    def find_cheapest_trip(self, shops: dict, FUEL_PRICE: float):
        prices_trips = {}
        cheapest_shop = {}
        for shop in shops:
            trip_price = round(self.calculate_trip_price(shop, FUEL_PRICE), 2)
            print(f"{self.name}'s trip to the {shop.name} "
                  f"costs {trip_price}")
            prices_trips[shop] = trip_price
        cheapest_shop["shop"] = \
            min(prices_trips, key=lambda name: prices_trips[name])
        cheapest_shop["costs"] = prices_trips[cheapest_shop["shop"]]
        return cheapest_shop

    def go_to_shop_trip(self, shop: Shop, cost: float):
        print(f"{self.name} rides to {shop.name}\n")
        shop.purchase(self.name, self.products.items())
        self.money -= cost
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money} dollars\n")
