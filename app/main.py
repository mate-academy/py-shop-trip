import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"])
        for customer in data["customers"]]
    shops = [
        Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        )
        for shop in data["shops"]
    ]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trips_price = sorted(
            [shop.count_trip_price(customer, fuel_price) for shop in shops],
            key=lambda x: x.trip_price
        )
        cheapest_shop = trips_price[0]
        if customer.money >= cheapest_shop.trip_price:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.make_purchases(cheapest_shop)
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make purchase in any shop")
