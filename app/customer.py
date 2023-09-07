import json
import os


current_directory = os.path.dirname(os.path.abspath(__file__))
relative_path = os.path.join(current_directory, "config.json")


def customers_and_content() -> list:
    with open(relative_path, "r") as file:
        content = json.load(file)
    customers = content.get("customers")
    return customers, content


class Customer:
    def __init__(self, content: dict) -> dict:
        self.content = content

    def customer_location() -> dict:
        customers, content = customers_and_content()
        customer = content.get("customers")
        priсe_fuel = content.get("FUEL_PRICE")
        fuel_consumption_car = {}
        location_customer = {}
        name_customer = []
        product_cart = {}
        money_custom = {}

        for elem_ in customer:
            name_cust = elem_.get("name")
            product_cart_ = elem_.get("product_cart")
            location_customer_ = elem_.get("location")
            fuel_consumption_car_ = elem_.get("car").get("fuel_consumption")
            money = elem_.get("money")
            location_customer.update({name_cust: location_customer_})
            fuel_consumption_car.update({name_cust: fuel_consumption_car_})
            product_cart.update({name_cust: product_cart_})
            money_custom.update({name_cust: money})
            name_customer.append(name_cust)

        return (
            location_customer,
            fuel_consumption_car,
            priсe_fuel,
            product_cart,
            money_custom,
            name_customer
        )
