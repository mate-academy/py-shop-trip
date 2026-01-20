from json import load
from os import path

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def get_data_from_json() -> dict:
    file_path = path.abspath("config.json")
    with open(file_path) as file:
        return load(file)


def init_customer(customer: dict) -> Customer:
    return Customer(
        name=customer["name"],
        product_cart=customer["product_cart"],
        location=customer["location"],
        money=customer["money"],
        car=get_instance_of_car(customer["car"]),
    )


def get_instance_of_car(car: dict) -> Car:
    return Car(brand=car["brand"], fuel_consumption=car["fuel_consumption"])


def init_shops(data: list) -> list[Shop]:
    return [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"],
        )

        for shop in data
    ]


def get_min_cost_and_current_shop(trip_costs: dict) -> list:
    min_cost = float("inf")
    current_shop = ""
    for key, value in trip_costs.items():
        if min_cost > value:
            min_cost = value
            current_shop = key

    return [min_cost, current_shop]


def shop_trip() -> None:
    data = get_data_from_json()
    fuel_price = data["FUEL_PRICE"]
    shops = init_shops(data["shops"])
    for customer in data["customers"]:
        customer = init_customer(customer)
        trip_costs = customer.get_all_trip_costs(shops, fuel_price)

        min_cost_and_current_shop_list = (
            get_min_cost_and_current_shop(trip_costs))

        min_cost = min_cost_and_current_shop_list[0]
        current_shop = min_cost_and_current_shop_list[1]

        if customer.money < min_cost:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
            continue

        customer.process_purchasing(
            current_shop=current_shop,
            min_cost=min_cost
        )
