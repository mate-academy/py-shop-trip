import math
from app.car import Car


class Customer:
    def __init__(self, name: str, product_cart: dict, location: list, money: float, car: Car):
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car

    def calculate_fuel_cost(self, destination, fuel_cost):
        x1, y1 = self.location
        x2, y2 = destination
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)

        fuel_needed = (distance / 100) * self.car.fuel_consumption
        total_fuel_cost = fuel_needed * fuel_cost * 2
        return total_fuel_cost

    def find_the_cheapest_shop(self, shops: list, fuel_cost: float):
        cheapest_total = 0
        shop_to_go = None
        for shop in shops:
            cost_of_fuel = self.calculate_fuel_cost(shop.location, fuel_cost)
            cost_of_products = shop.calculate_cart(self.product_cart)
            full_cost = round(cost_of_products + cost_of_fuel, 2)

            if not cheapest_total or full_cost < cheapest_total:
                cheapest_total = full_cost
                shop_to_go = shop

            print(f"{self.name}'s trip to the {shop.name} costs {full_cost}")

        return shop_to_go, cheapest_total

    def ride_to_shop(self, shop):
        print(f"{self.name} rides to {shop.name}\n")
        self.location = shop.location

    def ride_to_home(self, home):
        print(f"{self.name} rides home")
        self.location = home

    def count_money_after_shop(self, total_cost):
        self.money -= total_cost
        print(f"{self.name} now has {round(self.money, 2)} dollars\n")


def load_customers(file_data):
    customers = []

    for customer in file_data["customers"]:
        customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"],
            ),
        )
        customers.append(customer)

    return customers
