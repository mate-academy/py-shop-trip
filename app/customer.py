import math
import datetime

class Customer:
    def __init__(self, data: dict) -> None:
        self.name = data["name"]
        self.cart = data["product_cart"]
        self.location = data["location"]
        self.money = data["money"]
        self.car_brand = data["car"]["brand"]
        self.fuel_consumption = data["car"]["fuel_consumption"]

    def get_distance(self, shop_location: list) -> float:
        return math.sqrt(
            (self.location[0] - shop_location[0]) ** 2
            + (self.location[1] - shop_location[1]) ** 2
        )

    def calculate_trip_cost(self, shop, fuel_price: float) -> float:
        distance = self.get_distance(shop.location)
        fuel_needed = (2 * distance * self.fuel_consumption) / 100
        fuel_cost = fuel_needed * fuel_price
        product_cost = shop.calculate_products_cost(self.cart)
        return fuel_cost + product_cost

    def print_receipt(self, shop) -> None:
        now = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
        print(f"Date: {now}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought:")

        total_cost = 0
        for item, quantity in self.cart.items():
            price = shop.products[item] * quantity
            total_cost += price
            print(f"{quantity} {item}s for {round(price, 2)} dollars")

        print(f"Total cost is {round(total_cost, 2)} dollars")
        print("See you again!")
