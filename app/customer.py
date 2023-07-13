from dataclasses import dataclass
from .car import Car


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car


def make_list_of_instance(data: list) -> list:
    list_of_customers = []
    for cust_data in data:
        customer = Customer(
            cust_data["name"],
            cust_data["product_cart"],
            cust_data["location"],
            cust_data["money"],
            Car(
                cust_data["car"].get("brand"),
                cust_data["car"].get("fuel_consumption")
            )
        )
        list_of_customers.append(customer)
    return list_of_customers


def price_of_travel(
        customer_coord: list,
        fuel_consumption: float,
        location: list,
        fuel_price: float
) -> float:
    distance = ((((location[0] - customer_coord[0]) ** 2)
                 + ((location[1] - customer_coord[1]) ** 2)) ** 0.5)
    fuel_price_per_car = (round((((fuel_consumption / 100)
                                  * distance) * fuel_price) * 2, 2))
    return fuel_price_per_car
