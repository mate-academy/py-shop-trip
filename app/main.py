import json
import math
import datetime


class Shop:

    shops = []

    def __init__(self, shop: dict):
        self.name = shop["name"]
        self.location = shop["location"]
        self.products = shop["products"]
        Shop.shops.append(self)

    def buy_products(self, customer):
        total_cost = 0
        print(
            f"Date: {date_to_print()}\n"
            f"Thanks, {customer.name}, for you purchase!\n"
            f"You have bought: "
        )
        for product, count in customer.products.items():
            product_costs = count * self.products[product]
            total_cost += product_costs
            print(f"{count} {product}s for {product_costs} dollars")
        print(
            f"Total cost is {total_cost} dollars\n"
            f"See you again!\n"
        )


class Customer:

    customers = []

    def __init__(self, customer: dict):
        self.name = customer["name"]
        self.location = customer["location"]
        self.home_location = self.location
        self.products = customer["product_cart"]
        self.money = customer["money"]
        self.fuel_consumption = customer["car"]["fuel_consumption"]
        Customer.customers.append(self)

    def fuel_cost(self, destination, fuel_prise):
        x_sub = self.location[0] - destination[0]
        y_sub = self.location[1] - destination[1]
        distance_to_shop = math.sqrt(x_sub ** 2 + y_sub ** 2)
        fuel_count = distance_to_shop * self.fuel_consumption / 100
        fuel_cost = fuel_count * fuel_prise
        return fuel_cost

    def all_products_costs(self, shop):
        return sum(
            self.products[item] * shop.products[item]
            for item in self.products
        )

    def rides_to_shop(self, shop):
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def rides_home(self):
        self.location = self.home_location
        print(f"{self.name} rides home")


def date_to_print():
    date = datetime.datetime.now()
    return date.strftime("%d/%m/%Y %H:%M:%S")


def cheapest_trip(customer, fuel_price):
    cheapest_shop = None
    cost = 0
    for shop in Shop.shops:
        fuel_cost = customer.fuel_cost(shop.location, fuel_price) * 2
        trip_cost = customer.all_products_costs(shop) + fuel_cost
        print(f"{customer.name}'s trip to the "
              f"{shop.name} costs {round(trip_cost, 2)}")

        if cheapest_shop is None:
            cheapest_shop = shop
            cost = trip_cost

        if trip_cost < cost:
            cheapest_shop = shop
            cost = trip_cost
    return {"cheapest_shop": cheapest_shop, "cost": cost}


def shop_trip():
    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]

    for customer in data["customers"]:
        Customer(customer)
    for shop in data["shops"]:
        Shop(shop)

    for customer in Customer.customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop, cost = cheapest_trip(customer, fuel_price).values()
        if customer.money > cost:
            total_bill = customer.fuel_cost(
                cheapest_shop.location,
                fuel_price
            )
            customer.rides_to_shop(cheapest_shop)
            total_bill += customer.all_products_costs(cheapest_shop)
            cheapest_shop.buy_products(customer)
            total_bill += customer.fuel_cost(
                customer.home_location,
                fuel_price
            )
            customer.rides_home()
            balance = customer.money - round(total_bill, 2)
            print(f"{customer.name} now has {balance} dollars\n")
        else:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make purchase in any shop"
            )
