import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config = json.load(config_file)

    shops = config.get("shops")
    customers = config.get("customers")
    fuel_price = config.get("FUEL_PRICE")

    customers_list = []
    shops_list = []

    for customer in customers:
        car_info = customer["car"]
        brand = car_info["brand"]
        fuel_consumption = car_info["fuel_consumption"]

        customer_instance = Customer(
            name=customer["name"],
            products=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                brand=brand,
                fuel_consumption=fuel_consumption
            )
        )
        customers_list.append(customer_instance)

    for shop in shops:
        shop_instance = Shop(
            name=shop.get("name"),
            location=shop.get("location"),
            products=shop.get("products")
        )
        shops_list.append(shop_instance)

    for customer in customers_list:
        selected_shop = customer.define_shop(
            shops=shops_list,
            fuel_price=fuel_price
        )
        if selected_shop:
            customer.make_purchase(selected_shop=selected_shop)
            customer.ride_home()
