import json

from app.car.car import Car
from app.customers.customer import Customer
from app.products.products import Products
from app.shop.shop import Shop


def create_customers(dict_customers: dict):
    list_customers = []

    for customer in dict_customers:
        customer_car = Car(
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"],
        )

        obj_customer = Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer_car
        )

        list_customers.append(obj_customer)
    return list_customers


def create_shops(dict_shops: dict):
    list_shops = []

    for shop in dict_shops:
        list_products = []
        for name, cost in shop["products"].items():
            products = Products(name, cost)
            list_products.append(products)

        obj_shop = Shop(
            shop["name"],
            shop["location"],
            list_products,
        )

        list_shops.append(obj_shop)
    return list_shops


def shop_trip():
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = data["customers"]
    shops = data["shops"]

    customers = create_customers(customers)
    shops = create_shops(shops)

    for customer in customers:
        customer.trip(shops, fuel_price)


if __name__ == "__main__":
    shop_trip()
