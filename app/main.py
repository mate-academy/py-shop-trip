import json
from app.shop import Shop
from app.car import Car
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        config_data = json.load(config_file)
        fuel_price = config_data["FUEL_PRICE"]
        costumers_list = config_data["customers"]
        shops_list = config_data["shops"]

    for costumer in costumers_list:
        client = Customer(
            costumer["name"],
            costumer["product_cart"],
            costumer["location"],
            costumer["money"],
            costumer["car"],
        )
        client_car = Car(
            fuel_price,
            client.car["fuel_consumption"],
            client.location,
        )

        shops_calculate_with_trip = {}
        shops_calculate = {}
        print(f"{client.name} has {client.money} dollars")
        for shop_data in shops_list:
            shop = Shop(
                shop_data["name"],
                shop_data["location"],
                shop_data["products"],
            )
            shops_calculate[shop.shop_name] \
                = shop.calculate_product(client.product_cart)

            trip_cost = shop.sum_of_products(shops_calculate[shop.shop_name]) \
                + client_car.calculate_trip(shop.location_shop)

            shops_calculate_with_trip[shop.shop_name] = round(trip_cost, 2)

            print(f"{client.name}'s trip to the "
                  f"{shop.shop_name} costs {round(trip_cost, 2)}")

        cheapest_shop_name = \
            client.the_cheapest_trip_to_the_store(shops_calculate_with_trip)

        if shops_calculate_with_trip[cheapest_shop_name] > client.money:
            print(f"{client.name} doesn't have enough money "
                  f"to make purchase in any shop")
            continue
        print(f"{client.name} rides to {cheapest_shop_name}\n")

        shop_result = shops_calculate[cheapest_shop_name]
        client.print_check(shop_result, Shop.sum_of_products(shop_result))
        spent_money = shops_calculate_with_trip[cheapest_shop_name]
        print(f"{client.name} rides home")
        print(f"{client.name} now has {client.money - spent_money} dollars\n")
