import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)

    fuel_price = data.get("FUEL_PRICE")
    customers_data = data.get("customers")
    shops_data = data.get("shops")

    customers: list[Customer] = []
    shops: list[Shop] = []

    for customer in customers_data:
        customer_instance = Customer(
            customer.get("name"),
            customer.get("product_cart"),
            customer.get("location"),
            customer.get("money"),
            Car(
                customer.get("car").get("brand"),
                customer.get("car").get("fuel_consumption")
            ),
        )

        customers.append(customer_instance)

    for shop in shops_data:
        shop_instance = Shop(
            shop.get("name"),
            shop.get("location"),
            shop.get("products"),
        )

        shops.append(shop_instance)

    for customer in customers:
        selected_shop = customer.select_shop(shops, fuel_price)
        if selected_shop:
            customer.make_purchase(selected_shop)
            customer.ride_home()


shop_trip()
