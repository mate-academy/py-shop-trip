import json
from app.trip import Trip
from app.customer import Customer
from app.shop import Shop


def calculate_trips(customers: list[Customer],
                    shops: list[Shop],
                    fuel_price: float) -> None:
    for customer in customers:
        for shop in shops:
            customer.possible_trips.append(Trip(customer,
                                                shop,
                                                fuel_price))


def data_preparing(config: json) -> list:
    config = json_reading(config)
    costumers = [Customer(customer) for customer in config["customers"]]
    shops = [Shop(shop) for shop in config["shops"]]
    fuel_price = config["FUEL_PRICE"]
    return [costumers, shops, fuel_price]


def json_reading(file_path: str) -> dict:
    with open(file_path, "r") as file:
        data = file.read()
        py_dict = json.loads(data)
    return py_dict
