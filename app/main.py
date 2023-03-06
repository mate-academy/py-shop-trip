import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        data = json.load(file)
        fuel_price = data["FUEL_PRICE"]
        shops = [Shop(shop) for shop in data["shops"]]
        customers = [Customer(customer) for customer in data["customers"]]
        for customer in customers:
            the_shop = customer.select_the_shop(shops, fuel_price)
            if the_shop:
                customer.go_shopping(the_shop)
