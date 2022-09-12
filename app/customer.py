import math
from app.information import customers_information


class Customer:
    information = customers_information()

    @staticmethod
    def two_points(point_1: list, point_2: list) -> float:
        x_distance = point_2[0] - (point_1[0])
        y_distance = point_2[1] - (point_1[1])
        return math.sqrt(x_distance ** 2 + y_distance ** 2)

    @staticmethod
    def fuel_cost(fuel_price, fuel_consumption: float) -> float:
        price_of_100_km = fuel_price * fuel_consumption
        price_of_1_km = price_of_100_km / 100
        return price_of_1_km

    @staticmethod
    def checking_money(name: str, shops_name: str,
                       money: (int, float), total_cost: (int, float)):
        if money >= total_cost:
            print(f"{name} rides to {shops_name}")
            return
        print(f"{name} doesn't have enough money to make purchase in any shop")

    @staticmethod
    def person_money(name, money):
        print(f"{name} has {money} dollars")

    @staticmethod
    def trip_home(name: str, money: (int, float)):
        print(f"{name} rides home")
        print(f"{name} now has {money} dollars")
        print()
