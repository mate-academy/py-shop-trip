import json
import os
from app.car import Car


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_directory, "config.json")


def customers_and_content() -> list:
    with open(relative_path, "r") as file:
        content = json.load(file)
    customers = content.get("customers")
    shops = content.get("shops")
    priсe_fuel = content.get("FUEL_PRICE")
    return customers, content, shops, priсe_fuel


class CustomerCar:
    def __init__(
            self,
            name: str,
            product_cart: dict,
            location: list,
            money: int,
            car: list
    ) -> None:
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        self.car = Car(**car)

    def customer_location(self) -> dict:
        fuel_consumption_car = self.car
        distance_customer_x = self.location[0]
        distance_customer_y = self.location[1]
        product_cart = self.product_cart
        money = self.money
        name = self.name
        print(f"{name} has {money} dollars")

        return {
            "fuel_consumption_car": fuel_consumption_car,
            "distance_customer_x": distance_customer_x,
            "distance_customer_y": distance_customer_y,
            "product_cart": product_cart,
            "money": money,
            "name": name,
        }
