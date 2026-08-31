import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config: dict = json.load(file)
    fuel_price = config["FUEL_PRICE"]
    customers = [
        Customer(
            cust["name"],
            cust["product_cart"],
            cust["location"],
            cust["money"],
            Car(**cust["car"]),
        )
        for cust in config["customers"]
    ]
    shops = [Shop(**shop) for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        destination = customer.plan_trip(shops, fuel_price)
        if destination is None:
            print(
                f"{customer.name} doesn't have "
                f"enough money to make a purchase in any shop"
            )
            continue
        shop = destination[0]
        customer.ride_to(shop, destination[2])
        shop.serve(customer)
        customer.ride_home()
        print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
