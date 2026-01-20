import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)
        fuel_price = config["FUEL_PRICE"]

        for customer in config["customers"]:
            customer = Customer(customer)
            shops = [Shop(shop) for shop in config["shops"]]

            shop, trip_cost = customer.calculate_cheapest_shop_and_price(
                shops=shops,
                fuel_price=fuel_price
            )

            if shop is not None:
                customer.make_purchases(
                    shop=shop,
                    trip_cost=trip_cost
                )
