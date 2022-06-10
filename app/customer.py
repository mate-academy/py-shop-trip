from math import dist
# from datetime import datetime


class Customer:
    def __init__(self, name, product_cart, location, money, car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

        self.trips = {}
        self.cheapest_shop = None

    def drive_price(self, shops, fuel_price):
        for shop in shops:
            distance_to_shop = dist(self.location, shop.location)
            fuel_per_km = self.car["fuel_consumption"] / 100
            price = round(distance_to_shop * fuel_per_km * fuel_price * 2, 2)
            self.trips[shop.name] = price

    def shopping_price(self, shops):
        for shop in shops:
            shopping_expenses = 0
            for product, count in self.product_cart.items():
                shopping_expenses += shop.prices[product] * count
            self.trips[shop.name] += shopping_expenses

    def find_better_price(self, shops, fuel_price):
        self.drive_price(shops, fuel_price)
        self.shopping_price(shops)

        for index, price in enumerate(self.trips.values()):
            if price == min(self.trips.values()):
                self.cheapest_shop = shops[index]

    def do_shopping(self):
        shopping_price = 0
        # print(datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
        print("Date: 11/03/2020 13:15:34")
        print(f"Thanks, {self.name}, for you purchase!")
        print("You have bought: ")
        for product, count in self.product_cart.items():
            product_price = self.cheapest_shop.prices[product] * count
            shopping_price += product_price
            print(f"{count} {product}s for {product_price} dollars")
        print(f"Total cost is {shopping_price} dollars")
        print("See you again!\n")
