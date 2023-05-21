import json
from app.trip import can_afford_trip
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data.get("FUEL_PRICE", 0)

    customers_data = data.get("customers", [])
    customers = [
        Customer(
            customer.get("name"),
            customer.get("product_cart"),
            customer.get("location"),
            customer.get("money"),
            customer.get("car"),
        )
        for customer in customers_data
    ]

    shops = [
        Shop(shop.get("name"), shop.get("location"), shop.get("products"))
        for shop in data.get("shops", [])
    ]

    for customer in customers:
        can_afford_trip(customer, shops, fuel_price)
