import json
from app.car import Car
from app.customer import Customer
from app.Shop import Shop
import datetime
from typing import Type


def shop_trip() -> None:
    try:
        with open("app/config.json", "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError("Config file not found: app/config.json")

    fuel_price = config["FUEL_PRICE"]
    shops = {}

    for shop_data in config["shops"]:
        shop_name = shop_data["name"]
        shop_location = tuple(shop_data["location"])
        products = shop_data["products"]
        shops[shop_name] = Shop(shop_name, shop_location, products)

    customers = []

    for customer_data in config["customers"]:
        name = customer_data["name"]
        product_cart = customer_data["product_cart"]
        location = tuple(customer_data["location"])
        money = customer_data["money"]
        car_data = customer_data["car"]
        car = Car(car_data["brand"], car_data["fuel_consumption"])
        customers.append(Customer(name, product_cart, location, money, car))

    print("Starting shop trip simulation\n")

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        trip_costs = {}
        for shop_name, shop in shops.items():
            trip_cost = customer.calculate_trip_cost(shop.location, fuel_price)
            purchase_cost = shop.calculate_purchase_cost(customer.product_cart)
            total_cost = trip_cost * 2 + purchase_cost
            trip_costs[shop_name] = total_cost
            print(f"{customer.name}'s"
                  f" trip to the {shop_name} costs {total_cost: .2f}")

        cheapest_store_name = min(trip_costs, key=trip_costs.get)
        cheapest_store = shops[cheapest_store_name]

        total_cost = trip_costs[cheapest_store_name]
        if total_cost > customer.money:
            print(f"{customer.name}"
                  f" doesn't have enough money"
                  f" to make a purchase in any shop\n")
            continue

        if not cheapest_store.is_product_available(
                customer.product_cart):
            print(f"{customer.name} cannot purchase from {cheapest_store_name}"
                  f" due to product unavailability.\n")
            continue

        print(f"{customer.name} rides to {cheapest_store_name}")
        customer.location = cheapest_store.location

        purchase_cost = cheapest_store.calculate_purchase_cost(
            customer.product_cart)
        if customer.purchase(total_cost):
            print_receipt(customer.name, cheapest_store, purchase_cost)
        else:
            print(f"{customer.name}"
                  f" doesn't have enough money to complete the purchase.\n")
            continue

        print(f"{customer.name} rides home")
        customer.location = config["customers"][
            customers.index(customer)]["location"]
        print(f"{customer.name} now has {customer.money: .2f} dollars\n")


def print_receipt(self) -> None:
    print(f"Date: {datetime.datetime.now()}")
    print(f"Thanks, {self.name}, for your purchase!")
    print("You have bought:")
    for product, quantity in self.product_cart.items():
        if quantity > 0:
            print(f"{quantity} {product}(s)"
                  f" for {self.products[product] * quantity} dollars")

    total_cost = self.calculate_purchase_cost(self.product_cart)
    print(f"Total cost: {total_cost} dollars")
    print("See you again!")
