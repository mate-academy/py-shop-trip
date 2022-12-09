import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def read_customers(data: dict) -> list[Customer]:
    customers = []
    for customer in data["customers"]:
        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                Car(
                    customer["car"]["brand"],
                    customer["car"]["fuel_consumption"],
                ),
            )
        )
    return customers


def read_shops(data: dict) -> list[Shop]:
    shops = []
    for shop in data["shops"]:
        shops.append(Shop(shop["name"], shop["location"], shop["products"]))
    return shops


def shop_trip():
    with open("config.json") as cfg:
        data = json.load(cfg)

    customers = read_customers(data)
    shops = read_shops(data)
    fuel_price = data["FUEL_PRICE"]

    for customer in customers:
        customer.print_money()
        for shop in shops:
            customer.print_costs_trip(shop, fuel_price)
        customer.ride_to_shop(customer.get_cheaper_shop(shops, fuel_price))
        print("")


shop_trip()
