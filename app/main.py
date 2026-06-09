import json
import datetime
from math import sqrt
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    clients = []
    with open("app/config.json", "r") as config_file_json:
        json_data = json.load(config_file_json)

    for customer_data in json_data["customers"]:
        car = Car(**customer_data["car"])
        customer_data["car"] = car
        clients.append(
            Customer(**customer_data)
        )

    shops = [Shop(**shop_data) for shop_data in json_data["shops"]]
    fuel_price_data = json_data["FUEL_PRICE"]

    for client in clients:
        print(f"{client.name} has {client.money} dollars")
        shops_trip_cost = []
        for shop in shops:
            distance_to_the_store = sqrt(
                pow((client.location[0] - shop.location[0]), 2)
                + pow((client.location[1] - shop.location[1]), 2)
            )
            fuel_cost_to_the_store = (
                distance_to_the_store
                * client.car.fuel_consumption
                / 100 * fuel_price_data
            )
            cost_of_all_goods = sum(
                number * shop.products[product]
                for product, number in client.product_cart.items()
            )
            trip_cost = round(
                fuel_cost_to_the_store
                + cost_of_all_goods
                + fuel_cost_to_the_store, 2
            )
            shops_trip_cost.append((trip_cost, shop, cost_of_all_goods))
            print(f"{client.name}'s trip to the {shop.name} costs {trip_cost}")
        cheapest_shop = min(shops_trip_cost, key=lambda trip: trip[0])

        if client.money >= cheapest_shop[0]:
            print(f"{client.name} rides to {cheapest_shop[1].name}")
            client.location = cheapest_shop[1].location
            client.money -= cheapest_shop[0]
            data_object = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            print(f"\nDate: {data_object}")
            print(f"Thanks, {client.name}, for your purchase!")
            print("You have bought:")

            for product, number in client.product_cart.items():
                price = cheapest_shop[1].products[product]

                if number * price == int(number * price):
                    print(
                        f"{number} {product}s "
                        f"for {int(number * price)} dollars"
                    )
                else:
                    print(f"{number} {product}s for {number * price} dollars")

            print(f"Total cost is {cheapest_shop[2]} dollars")
            print("See you again!")
            print(f"\n{client.name} rides home")
            print(f"{client.name} now has {client.money} dollars\n")
        else:
            print(
                f"{client.name} doesn't have enough "
                f"money to make a purchase in any shop"
            )
