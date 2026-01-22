from dataclasses import dataclass

from app.car import Car, create_car_from_dict
from app.location import Location, create_location_from_list


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: Location
    money: int | float
    car: Car


def create_customer_from_dict(person: dict) -> Customer:
    return Customer(
        name=person["name"],
        product_cart=person["product_cart"],
        location=create_location_from_list(person["location"]),
        money=person["money"],
        car=create_car_from_dict(person["car"])
    )
