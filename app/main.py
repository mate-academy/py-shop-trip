import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as file:
        config = json.load(file)

        customers = [
            Customer(
                person["name"],
                person["product_cart"],
                person["location"],
                person["money"],
                Car(config["FUEL_PRICE"],
                    person["car"]["brand"],
                    person["car"]["fuel_consumption"])
            )
            for person in config["customers"]
        ]

    shops = [
        Shop(place["name"], place["location"], place["products"])
        for place in config["shops"]
    ]

    for customer in customers:

        cheapest_shop = {}
        print(f"{customer.name} has {customer.money} dollars")

        for shop in shops:

            distance = shop.distance(customer.location)
            fuel = customer.car.fuel(distance)
            products_price = customer.products_price(shop)

            total_price = round(fuel + products_price, 2)
            cheapest_shop[total_price] = [shop, total_price]

            print(f"{customer.name}'s trip to "
                  f"the {shop.name} costs {total_price}")

            visited_shop = cheapest_shop[min(cheapest_shop.keys())]
            lowest_price = customer.products_price(visited_shop[0])

        if customer.money > visited_shop[1]:
            print(f"{customer.name} rides to {visited_shop[0].name}\n")

            home = customer.location

            customer.location = shop.location
            customer.buying_products(visited_shop[0])

            print(f"Total cost is {lowest_price} dollars"
                  "\nSee you again!\n")

            customer.location = home

            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has"
                  f"{customer.money - visited_shop[1]: .2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")


shop_trip()
