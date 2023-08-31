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
    def __init__(
        self, content: dict, name: str, product_cart: dict,
            location: list, money: int, car: dict
    ) -> list:
        self.content = content
        self.name = name
        self.product_cart = product_cart
        self.location = location
        self.money = money
        self.car = car
        (
            self.location_customer1,
            self.fuel_consumption_car3,
            self.priсe_fuel,
            self.product_cart3,
            self.money_costum
        ) = self.customer_location()

    def customer_location() -> dict:
        customers, content = customers_and_content()
        customer = content.get("customers")
        priсe_fuel = content.get("FUEL_PRICE")
        fuel_consumption_car3 = {}
        location_customer1 = {}
        name_custom = {}
        count_ = 0

        product_cart3 = {}
        money_costum = {}

        # self.car = car
        for elem_ in customer:
            count_ += 1
            name_cust = elem_.get("name")
            product_cart = elem_.get("product_cart")
            location_customer = elem_.get("location")
            fuel_consumption_car = elem_.get("car").get("fuel_consumption")
            money = elem_.get("money")
            location_customer1.update({count_: location_customer})
            fuel_consumption_car3.update({count_: fuel_consumption_car})
            product_cart3.update({count_: product_cart})
            money_costum.update({count_: money})
            name_custom.update({count_: name_cust})

        return (
            location_customer1,
            fuel_consumption_car3,
            priсe_fuel,
            product_cart3,
            money_costum,
            name_custom
        )
