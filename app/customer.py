from dataclasses import dataclass
from app.car import Car, create_car
import math
from app.shop import Shop


@dataclass
class Customer:
    name: str
    products_to_buy: dict
    location: list
    money: int
    car: Car

    def choose_shop(self, shops_list: list, fuel_price: float | int) -> tuple:
        best_shop = None
        min_cost = float("inf")
        best_fuel_cost = None
        for shop in shops_list:
            distance = math.sqrt(
                (shop.location[0] - (self.location[0])) ** 2
                + (shop.location[1] - (self.location[1])) ** 2
            )
            products_cost = shop.calculate_product_cost(self)
            trip_fuel_cost = self.car.calculate_fuel_cost(distance * 2,
                                                          fuel_price)
            total_trip_cost = trip_fuel_cost + products_cost
            total_trip_cost = round(total_trip_cost, 2)
            print(f"{self.name}'s trip to the "
                  f"{shop.name} costs {total_trip_cost}")
            if self.money >= total_trip_cost:
                if total_trip_cost < min_cost:
                    min_cost = total_trip_cost
                    best_shop = shop
                    best_fuel_cost = trip_fuel_cost
        if best_shop is None:
            print(f"{self.name} doesn't have enough "
                  f"money to make a purchase in any shop")
        return best_shop, best_fuel_cost

    def ride_to(self, shop: Shop) -> None:
        self.home = self.location
        self.location = shop.location
        print(f"{self.name} rides to {shop.name}\n")

    def ride_home(self, home: list) -> None:
        self.location = home
        print(f"{self.name} rides home\n"
              f"{self.name} now has {round(self.money, 2)} dollars\n")


def create_customer(customers_data: list) -> list[Customer]:
    customers_list = []
    for customer in customers_data:
        customers_list.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            create_car(customer["car"]),
        ))
    return customers_list
