import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as conf_file:
        conf_json_file = json.load(conf_file)
    fuel_price = conf_json_file["FUEL_PRICE"]

    for item in conf_json_file["customers"]:
        customer = Customer(
            name=item["name"],
            product_cart=item["product_cart"],
            location=item["location"],
            money=item["money"]
        )

        car = Car(
            fuel_consumption=item["car"]["fuel_consumption"],
            fuel_price=fuel_price
        )

        print(f"{customer.name} has {customer.money} dollars")
        min_price, name_shop = customer.money, ""

        for shop in conf_json_file["shops"]:
            price_shop = Shop(
                name=shop["name"],
                location=shop["location"],
                cost_products=shop["products"],
            )
            price = customer.price_trip_in_shop(car, price_shop)
            if price < min_price:
                min_price, name_shop = price, price_shop

        if min_price != customer.money:
            customer.buy_in_the_shop(min_price, name_shop)
        else:
            print(
                f"{customer.name} "
                f"doesn't have enough money to make a "
                f"purchase in any shop"
            )


shop_trip()
