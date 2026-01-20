import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        info = json.load(file)
        shops = info["shops"]
        customers = info["customers"]
        fuel_price = info["FUEL_PRICE"]
        list_of_shops = []

        for shop in shops:
            shop = Shop(
                name=shop["name"],
                location=shop["location"],
                products=shop["products"]
            )
            list_of_shops.append(shop)

        for data in customers:
            customer = Customer(
                name=data["name"],
                product_cart=data["product_cart"],
                location=data["location"],
                money=data["money"],
                car=data["car"])

            print(customer.__str__())

            customer.shopping(list_of_shops, fuel_price)
