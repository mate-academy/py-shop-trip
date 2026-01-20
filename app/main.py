import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=customer["car"])
        for customer in data["customers"]
    ]
    shops = [
        Shop(
            name=shop["name"],
            location=shop["location"],
            products=shop["products"]
        )
        for shop in data["shops"]
    ]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trips_price = [
            shop.count_trip_price(customer, fuel_price)
            for shop in shops
        ]
        cheapest_shop = min(trips_price, key=lambda x: x.trip_price)
        if customer.money >= cheapest_shop.trip_price:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.make_purchases(cheapest_shop)
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make purchase in any shop")
