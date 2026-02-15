import json
import datetime

from dataclasses import dataclass
from math import sqrt
from pathlib import Path
from app.shop import Shop


@dataclass
class Car:
    brand: str
    fuel_consumption: float


@dataclass
class Customer:
    name: str
    product_cart: dict
    location: list
    money: int
    car: Car

    @classmethod
    def from_dict(cls, data: dict) -> "Customer":
        data["car"] = Car(**data["car"])
        return cls(**data)


with open(Path(__file__).resolve().parent / "config.json") as data_file:
    data_main = json.load(data_file)

customers = [
    Customer.from_dict(customer)
    for customer in data_main["customers"]
]
shops = [Shop(**item) for item in data_main["shops"]]
fuel_price = data_main["FUEL_PRICE"]


def distance(point1: list, point2: list) -> float:
    return sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)


def fuel_cost_for_distance(
        dist_km: float,
        fuel_consumption_per_100km: float
) -> float:
    liters = dist_km * (fuel_consumption_per_100km / 100)
    return liters * fuel_price


def format_output(number: int | float) -> str:
    value = round(number, 2)
    if isinstance(value, int):
        return str(int(value))
    return f"{value:.2f}".rstrip("0").rstrip(".")


def product_cost(product_cart: dict, products: dict) -> float:
    cost = 0
    for name, amount in product_cart.items():
        if name in products:
            cost += amount * products[name]
    return cost


def bill_from_the_shop(customer: Customer, shop: Shop) -> None:

    print(f"\nDate: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}")
    print(f"Thanks, {customer.name}, for your purchase!")
    print("You have bought:")
    for product, amount in customer.product_cart.items():
        price = shop.products[product]
        print(
            f"{amount} {product}s for "
            f"{format_output(amount * price)} dollars"
        )
    prod_cost = product_cost(
        customer.product_cart,
        shop.products
    )
    print(f"Total cost is {format_output(prod_cost)} dollars")
    print("See you again!\n")
