from datetime import datetime
from helpers import calculate_distance


class Shop:
    def __init__(self, name, location, products):
        self.name = name
        self.location = location
        self.products = products

    def get_products_cost(self, cart):
        return sum(self.products[item] * count for item, count in cart.items())


class Customer:
    def __init__(self, data):
        self.name = data["name"]
        self.cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car = data["car"]

    def calculate_trip_costs(self, shop, fuel_price):
        dist = calculate_distance(self.location, shop.location)
        fuel_one_way = (dist / 100) * self.car["fuel_consumption"] * fuel_price
        total_fuel = fuel_one_way * 2
        products_cost = shop.get_products_cost(self.cart)

        return {
            "total": total_fuel + products_cost,
            "fuel_only": total_fuel,
            "products_only": products_cost
        }

    def print_receipt(self, shop, costs):
        print(f"Date: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")
        for item, count in self.cart.items():
            price = shop.products[item] * count
            print(f"{count} {item}{'s' if count > 1 else ''} for {price} dollars")

        print(f"Total cost is {costs['products_only']} dollars")
        print("See you again!")
