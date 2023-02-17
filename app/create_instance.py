from typing import List

from app.car import Car
from app.customer import Customer
from app.location import Location
from app.product import Product
from app.shop import Shop


def create_customers(customers_dict: dict, ) -> List[Customer]:
    customers = []
    for customer in customers_dict:
        location = Location(x_axis=customer["location"][0],
                            y_axis=customer["location"][1])
        car = Car(brand=customer["car"]["brand"],
                  fuel_consumption=customer["car"]["fuel_consumption"])
        customer = Customer(name=customer["name"],
                            product_cart=customer["product_cart"],
                            location=location,
                            money=customer["money"],
                            car=car)
        customers.append(customer)

    return customers


def create_shops(shops_dict: dict) -> List[Shop]:
    shops = []
    for shop in shops_dict:
        location = Location(x_axis=shop["location"][0],
                            y_axis=shop["location"][1])
        products = {
            name: Product(name=name, price=price)
            for name, price in shop["products"].items()
        }
        shop = Shop(name=shop["name"],
                    location=location,
                    products=products)
        shops.append(shop)

    return shops
