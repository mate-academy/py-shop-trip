import json

from app.modules.customer import Customer
from app.modules.shop import Shop
from app.utils.main import calculate_trip_cost, shop_in_store


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price: float = config["FUEL_PRICE"]
    customers: list[Customer] = config["customers"]
    shops: list[Shop] = config["shops"]

    for customer in customers:
        print(f'{customer["name"]} has {customer["money"]} dollars')

        shopping_price: dict[str, float] = {}

        for shop in shops:
            shopping_price[shop["name"]] = calculate_trip_cost(
                customer,
                shop,
                fuel_price
            )

            print(
                f"{customer["name"]}'s trip to the {shop["name"]} "
                f'costs {shopping_price[shop["name"]]}'
            )

        cheapest_shop_name = min(shopping_price, key=shopping_price.get)

        if shopping_price[cheapest_shop_name] > customer["money"]:
            print(
                f'{customer["name"]} doesn\'t have'
                f" enough money to make a purchase in any shop"
            )
            continue

        cheapest_shop = next(
            shop for shop in shops
            if shop["name"] == cheapest_shop_name
        )

        home_location = customer["location"]
        customer["location"] = cheapest_shop["location"]
        print(f'{customer["name"]} rides to {cheapest_shop_name}\n')

        shop_in_store(customer, cheapest_shop)

        customer["location"] = home_location
        print(f'{customer["name"]} rides home')
        customer["money"] -= round(shopping_price[cheapest_shop_name], 2)

        print(f'{customer["name"]} now has {customer["money"]} dollars\n')
