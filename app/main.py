import json
import datetime
from math import sqrt, inf


class Car:
    def __init__(self, brand, fuel):
        self.brand = brand
        self.fuel_consumption_one_km = fuel

    @staticmethod
    def from_dict(data):
        car = Car(
            data["brand"],
            data["fuel_consumption"] / 100
        )

        return car


class Customer:
    def __init__(self,
                 name: str,
                 location: list,
                 money: float,
                 car: Car,
                 product_cart: dict):
        self.name = name
        self.location = location
        self.money = money
        self.car = car
        self.product_cart = product_cart

    @staticmethod
    def from_dict(data):
        customer = Customer(
            data["name"],
            data["location"],
            data["money"],
            Car.from_dict(data["car"]),
            data["product_cart"])
        return customer


class Shop:
    def __init__(self,
                 name: str,
                 location: list,
                 products: dict):
        self.name = name
        self.location = location
        self.products = products

    @staticmethod
    def from_dict(data):
        shop = Shop(data["name"],
                    data["location"],
                    data["products"]
                    )
        return shop


with open("app/config.json") as f:
    INCOME_DATA = json.load(f)
FUEL_PRICE = INCOME_DATA["FUEL_PRICE"]


def calculate_visit(shop: Shop, customer: Customer):
    res = 0
    for key, value in customer.product_cart.items():
        if key in shop.products:
            res += value * shop.products[key]
    return res


def get_distance_round_trip(coord_from, coord_to):
    x = coord_from[1] - coord_to[1]
    y = coord_from[0] - coord_to[0]
    distance = sqrt(x**2 + y**2)
    return distance * 2


def shop_trip():
    customers = []
    shops = []
    for item in INCOME_DATA["customers"]:
        customer = Customer.from_dict(item)
        customers.append(customer)

    for item in INCOME_DATA["shops"]:
        shops.append(Shop.from_dict(item))
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
            cost = calculate_visit(shop, customer)
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
        for key, value in product_cart.items():
            print(f"{value} {key}s for "
                  f"{value * shop_price[key]} "
                  f"dollars")
        print(f"Total cost is {round(min_cost - mem_fuel_cost, 2)} dollars")
        print("See you again!\n")
        print(f"{customer.name} rides home")
        print(f"{customer.name} "
              f"now has "
              f"{round(customer.money - min_cost, 2)} "
              f"dollars")
