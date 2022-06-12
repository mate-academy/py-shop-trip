import json

from app.customer import Customer

from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
print(BASE_DIR)

def shop_trip():
    with open(BASE_DIR / "config.json", "r") as config:
        configs = json.load(config)
        fuel_price = configs["FUEL_PRICE"]
        customers = configs["customers"]
        shops = configs["shops"]

    for customer in customers:
        client = Customer(
            customer["name"],
            customer["money"],
            customer["location"],
            customer["product_cart"],
            customer["car"]["brand"],
            customer["car"]["fuel_consumption"]
        )
        variants_for_shoping = {}

        print(f"{client.name} has {client.money} dollars")

        for shop in shops:
            trip_price = client.calculate_trip_price(
                fuel_price,
                shop["location"]
            )
            bill, price_for_products = client.calculate_price_for_products(
                shop["products"]
            )

            print(f"{client.name}'s trip to the "
                  f"{shop['name']} costs "
                  f"{trip_price + price_for_products:.2f}")

            variants_for_shoping[price_for_products + trip_price] = {
                "name": shop["name"],
                "trip_price": trip_price,
                "bill": bill
            }

        smallest_price = min([key for key in variants_for_shoping.keys()])

        if smallest_price > client.money:
            print(f"{client.name} doesn't have enough money"
                  f" to make purchase in any shop")
        else:
            client.print_shoping_message(
                smallest_price,
                variants_for_shoping[smallest_price]["trip_price"],
                variants_for_shoping[smallest_price]["bill"],
                variants_for_shoping[smallest_price]["name"]
            )

shop_trip()
