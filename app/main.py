import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as config_file:
        config_info = json.load(config_file)

    fuel_price = config_info["FUEL_PRICE"]

    customers = []
    for customer in config_info["customers"]:
        customers.append(
            Customer(
                customer["name"],
                customer["product_cart"],
                customer["location"],
                customer["money"],
                customer["car"]
            )
        )

    shops = []
    for shop in config_info["shops"]:
        shops.append(
            Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
        )

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        best_shop = [shops[0], customer.trip_price(fuel_price, shops[0])]
        for shop in shops:
            trip_price = customer.trip_price(fuel_price, shop)
            if trip_price < best_shop[1]:
                best_shop[0] = shop
                best_shop[1] = trip_price

            print(
                f"{customer.name}'s trip to the {shop.name} "
                f"costs {round(customer.trip_price(fuel_price, shop), 2)}"
            )

        if customer.money < customer.trip_price(fuel_price, best_shop[0]):
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            break

        initial_coordinates = customer.location
        print(f"{customer.name} rides to {best_shop[0].name}")
        customer.location = shop.location

        print(best_shop[0].receipt(customer))

        customer.location = initial_coordinates
        customer.money -= customer.trip_price(fuel_price, best_shop[0])
        print(f"{customer.name} rides home\n"
              f"{customer.name} now has {round(customer.money, 2)} dollars\n")
