from typing import Union
from math import dist


class Customer:
    def __init__(self, name: str, money: Union[int, float]) -> None:
        self.name = name
        self.money = money

    def print_money(self) -> None:
        print(f"{self.name} has {self.money} dollars")

    def distance_calculation(self, location: list, shops: list) -> list:
        distance_to_shops = []
        for shop in shops:
            distance = dist(location, shop["location"])
            distance_to_shops.append(dict([
                ("store name", shop["name"]),
                ("distance", distance)
            ]))
        return distance_to_shops

    def can_make_a_trip(self, trip: dict) -> bool:
        if self.money > trip["cost of the trip"]:
            print(f"{self.name} rides to {trip['store name']}")
            return True
        else:
            print(f"{self.name} doesn't "
                  f"have enough money to make purchase in any shop")
            return False

    def return_home(self, trip: dict) -> None:
        print(f"{self.name} rides home")
        print(f"{self.name} now has {self.money - trip['cost of the trip']} "
              f"dollars", end="\n\n")
