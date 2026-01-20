from typing import List

from app.customer import Customer
from app.car import Car
from app.shop import Shop


def create_customers(customers_dict: List[dict]) -> List[Customer]:
    customers_from_data = []

    for customer in customers_dict:
        customers_from_data.append(
            Customer(
                name=customer.get("name"),
                product_cart=customer.get("product_cart"),
                location=customer.get("location"),
                money=customer.get("money"),
                car=Car(
                    brand=customer.get("car")["brand"],
                    fuel_consumption=customer.get("car")["fuel_consumption"]
                )
            )
        )

    return customers_from_data


def create_shops(shops_dict: List[dict]) -> List[Shop]:
    shops_from_data = []

    for shop in shops_dict:
        shops_from_data.append(
            Shop(
                name=shop.get("name"),
                location=shop.get("location"),
                products=shop.get("products")
            )
        )

    return shops_from_data
