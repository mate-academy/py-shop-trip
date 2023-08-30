import json
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_directory, "config.json")


def customers_and_content() -> list:
    with open(relative_path, "r") as file:
        global content
        content = json.load(file)
    global customers
    customers = content.get("customers")
    return customers, content


class Customer:
    def __init__(self, content: dict) -> list:
        self.content = content

    def customer_location() -> dict:
        customers, content = customers_and_content()
        customer = content.get("customers")
        priсe_fuel = content.get("FUEL_PRICE")
        fuel_consumption_car3 = {}
        location_customer1 = {}
        number = 0
        for elem_ in customer:
            number += 1
            location_customer = elem_.get("location")
            fuel_consumption_car = elem_.get("car").get("fuel_consumption")
            location_customer1.update({number: location_customer})
            fuel_consumption_car3.update({number: fuel_consumption_car})
        return location_customer1, fuel_consumption_car3, priсe_fuel
