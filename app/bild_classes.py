from json import load
from typing import Type

from app.customers.customer import CustomerCar, Customer
from app.shops.shop import Shop
from app.days.day import DayMark


def load_json_data(data: str) -> dict:
    with open(data) as json_data:
        return load(json_data)


def write_class_attrs(attrs_dict: dict, data: dict) -> dict:
    for data_key, data_value in data.items():
        if data_key in attrs_dict:
            attrs_dict[data_key] = data_value
    return attrs_dict


def fill_class_attrs(cls: Type,
                     data: dict) -> dict:
    attrs = dict.fromkeys(cls.__annotations__)
    cls_params = write_class_attrs(attrs, data)
    return cls_params


def create_customers(json_data: str) -> list[Customer]:
    output = []
    data = load_json_data(json_data)
    customers = data["customers"]
    for customer in customers:
        car_data = fill_class_attrs(CustomerCar,
                                    customer["car"])
        customer_car = CustomerCar(**car_data)
        customer_data = fill_class_attrs(Customer,
                                         customer)
        customer_data["car"] = customer_car
        person = Customer(**customer_data)
        output.append(person)
    return output


def create_shops(json_data: str) -> list[Shop]:
    data = load_json_data(json_data)
    shops = data["shops"]
    output = []
    for shop in shops:
        shop_data = fill_class_attrs(Shop, shop)
        current_shop = Shop(**shop_data)
        output.append(current_shop)
    return output


def create_day_mark(json_data: str, date: str) -> DayMark:
    data = load_json_data(json_data)
    fuel_price = data["FUEL_PRICE"]
    return DayMark(fuel_price=fuel_price, date=date)
