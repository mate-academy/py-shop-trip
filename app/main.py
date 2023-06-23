import json
from app.customer import Customer
from app.shop import Shop, calculate_trip_price, check_best_price
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as config:
        data = json.load(config)
        customers_data = data["customers"]
        shops_data = data["shops"]
        fuel_price = data["FUEL_PRICE"]

    for one_customer in customers_data:
        trip_prices = {}
        shops = {}

        client = Customer(one_customer["name"],
                          one_customer["product_cart"],
                          one_customer["location"],
                          one_customer["money"])
        print(f"{client.name} has {client.money} dollars")
        car = Car(one_customer["car"]["brand"],
                  one_customer["car"]["fuel_consumption"])
        for one_shop in shops_data:
            shop = Shop(one_shop["name"],
                        one_shop["location"],
                        one_shop["products"])
            trip_prices[shop.name] = calculate_trip_price(
                fuel_price,
                client,
                shop,
                car)
            shops[shop.name] = shop
        check_best_price(trip_prices, client, shops)
