import json
import math
from datetime import datetime


class Shop:

    shops = []

    def __init__(self, shop: dict):
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]
        Shop.shops.append(self)


class Customer:

    customers = []

    def __init__(self, customer: dict):
        self.name = customer["name"]
        self.location = customer["location"]
        self.products = customer["product_cart"]
        self.money = customer["money"]
        self.fuel_consumption = customer["car"]["fuel_consumption"]
        Customer.customers.append(self)

    def fuel_cost(self, shop, fuel_prise):
        x_sub = self.location[0] - shop.location[0]
        y_sub = self.location[1] - shop.location[1]
        distance_to_shop = math.sqrt(x_sub ** 2 + y_sub ** 2)
        fuel_count = distance_to_shop * self.fuel_consumption * 2 / 100
        fuel_cost = round(fuel_count * fuel_prise, 2)
        return fuel_cost

    def all_products_costs(self, shop):
        return sum(
            self.products[item] * shop.products[item]
            for item in self.products
        )


def shop_trip():
    with open("config.json", "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]

    for customer in data["customers"]:
        Customer(customer)
    for shop in data["shops"]:
        Shop(shop)

    for customer in Customer.customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        cheapest = 0

        for shop in Shop.shops:
            fuel_cost = customer.fuel_cost(shop, fuel_price)
            trip_cost = customer.all_products_costs(shop) + fuel_cost
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")

            if cheapest_shop is None:
                cheapest_shop = shop
                cheapest = trip_cost

            if trip_cost < cheapest:
                cheapest_shop = shop
                cheapest = trip_cost

        if customer.money > cheapest:
            date = datetime.strftime(datetime.now(), '%Y/%m/%d %H:%M:%S')
            print(
                f"{customer.name} rides to {cheapest_shop.name}\n\n"
                f"Date {date}\n"
                f"Thanks, {customer.name}, for you purchase!\nYou have bought:"
            )
            total_cost = 0

            for product, count in customer.products.items():
                product_costs = count * cheapest_shop.products[product]
                total_cost += product_costs
                print(f"{count} {product}s for {product_costs}")
            print(
                f"Total cost is {total_cost} dollars\n"
                f"See you again!\n\n"
                f"{customer.name} rides home\n"
                f"{customer.name} now has {customer.money - total_cost}\n"
            )
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make purchase in any shop"
            )
