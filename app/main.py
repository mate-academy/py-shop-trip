import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        json_data = json.load(file)

    customers = (Customer(customer) for customer in json_data["customers"])
    shops = [Shop(shop) for shop in json_data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        customer.all_shops_costs = {}

        for shop in shops:
            total_shopping_cost = customer.total_shopping_cost(
                shop, json_data["FUEL_PRICE"]
            )
            customer.all_shops_costs.update({shop: total_shopping_cost})
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {total_shopping_cost}")

        cheapest_shop = {
            "shop": min(customer.all_shops_costs,
                        key=customer.all_shops_costs.get),
            "products_cost": min(customer.all_shops_costs.values())
        }

        if customer.money >= cheapest_shop["products_cost"]:
            print(f"{customer.name} rides to {cheapest_shop['shop'].name}\n")
            customer.drive_to(cheapest_shop["shop"])
            customer.buy_products(cheapest_shop["shop"].products)
            customer.get_receipt()
            customer.count_remaining_money(cheapest_shop["products_cost"])
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
