import math
import datetime

from app.car import Car


class Customer:
    def __init__(
        self,
        config: dict
    ) -> None:
        self.name = config["name"]
        self.product_cart = config["product_cart"]
        self.location = config["location"]
        self.money = config["money"]
        self.car = Car(config["car"])

    @staticmethod
    def calculate_distance(location1: list, location2: list) -> float:
        x1, y1 = location1
        x2, y2 = location2
        distance = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
        return distance

    @staticmethod
    def calculate_fuel_cost(
        fuel_consumption: float,
        distance: float,
        fuel_price: float
    ) -> float:
        fuel_cost = (fuel_consumption / 100) * distance * fuel_price
        return fuel_cost

    @staticmethod
    def calculate_products_cost(
        product_cart: dict,
        products_price: dict
    ) -> list:
        milk_price = product_cart["milk"] * products_price["milk"]
        bread_price = product_cart["bread"] * products_price["bread"]
        butter_price = product_cart["butter"] * products_price["butter"]
        return [milk_price, bread_price, butter_price]

    def prints_purchase_receipt(self, product_price: dict) -> None:
        product_price = self.calculate_products_cost(
            self.product_cart,
            product_price
        )
        print()
        print(f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
        print(f"Thanks, {self.name}, for your purchase!")
        print("You have bought: ")

        index = 0
        for product_name, count in self.product_cart.items():
            print(f"{count} {product_name}s "
                  f"for {product_price[index]} dollars")
            index += 1

        print(f"Total cost is "
              f"{sum(product_price)} dollars")
        print("See you again!")
        print()
