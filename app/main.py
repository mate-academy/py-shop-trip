import json
from app.trip import Trip
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json") as config:
        data = json.load(config)
    fuel_price = data["FUEL_PRICE"]
    customers = [
        Customer(
            data["customers"][number]["name"],
            data["customers"][number]["product_cart"],
            data["customers"][number]["location"],
            data["customers"][number]["money"],
            data["customers"][number]["car"]
        )
        for number, customer in enumerate(data["customers"])]
    shops = [
        Shop(
            data["shops"][number]["name"],
            data["shops"][number]["location"],
            data["shops"][number]["products"],
        )
        for number, shop in enumerate(data["shops"])]

    for customer in customers:
        print(Trip.get_money(customer))
        cheapest_shop = Trip.choosing_the_cheapest_shop(
            customer, shops, fuel_price
        )
        if not cheapest_shop:
            print(
                (f"{customer.name}doesn't have enough money "
                 f"to make purchase in any shop")
            )
            break

        print(
            (f"{customer.name} rides to "
             f"{cheapest_shop}\n")
        )
        print(Trip.shopping(cheapest_shop, customer))
