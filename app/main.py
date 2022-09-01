import json
import datetime
from math import sqrt, inf


class Car:
    brand: str
    fuel_consumption_one_km: float

    def from_dict(self, data):
        self.brand = data["brand"]
        self.fuel_consumption_one_km = data["fuel_consumption"] / 100

        return self


class Product:
    milk: int = 0
    bread: int = 0
    butter: int = 0

    def from_dict(self, data):
        self.milk = data["milk"]
        self.bread = data["bread"]
        self.butter = data["butter"]
        return self

    def __mul__(self, other):
        sum_milk = self.milk * other.milk
        sum_bread = self.bread * other.bread
        sum_butter = self.butter * other.butter
        return sum_milk + sum_bread + sum_butter

    def getattr(self, item):
        return self.__getattribute__(item)


class Customer:
    name: str
    location: []
    money: int
    car: Car
    product_cart: Product()

    def from_dict(self, data):
        self.name = data["name"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = Car().from_dict(data["car"])
        self.product_cart = Product().from_dict(data["product_cart"])
        return self


class Shop:
    name: str
    location: []
    products: Product

    def from_dict(self, data):
        self.name = data["name"]
        self.location = data["location"]
        self.products = Product().from_dict(data["products"])
        return self


with open("app/config.json") as f:
    INCOME_DATA = json.load(f)
FUEL_PRICE = INCOME_DATA["FUEL_PRICE"]


def get_distance_round_trip(coord_from, coord_to):
    x = coord_from[1] - coord_to[1]
    y = coord_from[0] - coord_to[0]
    distance = sqrt(x**2 + y**2)
    return distance * 2


def shop_trip():
    customers = []
    shops = []
    for item in INCOME_DATA["customers"]:
        try:
            customer = Customer().from_dict(item)
            customers.append(customer)
        except Exception as e:
            print(item)
            print(e)
    for item in INCOME_DATA["shops"]:
        shops.append(Shop().from_dict(item))
    has_output = False
    for customer in customers:
        min_cost = inf
        best_shop = None
        mem_fuel_cost = 0
        if has_output:
            print("")
        has_output = True
        print(f"{customer.name} has {customer.money} dollars")
        for shop in shops:
            distance = get_distance_round_trip(customer.location,
                                               shop.location)
            cost = customer.product_cart * shop.products
            car = customer.car
            fuel_cost = FUEL_PRICE * car.fuel_consumption_one_km * distance
            cost_with_fuel = round(cost + fuel_cost, 2)
            if cost_with_fuel < customer.money\
                    and cost_with_fuel < min_cost:
                min_cost = cost_with_fuel
                best_shop = shop
                mem_fuel_cost = round(fuel_cost, 2)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {cost_with_fuel}")
        if best_shop is None:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
            continue
        print(f"{customer.name} rides to {best_shop.name}")
        print("")
        cur_date = datetime.datetime.now()
        print(f"Date: {cur_date.strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {customer.name}, for you purchase!")
        print("You have bought: ")
        product_cart = customer.product_cart
        shop_price = best_shop.products
        for attr in ["milk", "bread", "butter"]:
            print(f"{product_cart.getattr(attr)} {attr}s for "
                  f"{product_cart.getattr(attr) * shop_price.getattr(attr)} "
                  f"dollars")
        print(f"Total cost is {round(min_cost - mem_fuel_cost, 2)} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(f"{customer.name} "
              f"now has "
              f"{round(customer.money - min_cost, 2)} "
              f"dollars")
