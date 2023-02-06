import json
from app.customer import Customer
from app.shop import Shop
import os


def shop_trip() -> None:
    json_path = ""
    if "app" in os.getcwd():
        json_path = "config.json"
    else:
        json_path = "app/config.json"

    with open(json_path, "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = []
    for customer in data["customers"]:
        customers.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            customer["car"]
        ))

    shops = []
    for shop in data["shops"]:
        shops.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))

    for customer in customers:
        customer.balance_customer()

        list_cost = []
        for shop in shops:
            trip_cost = customer.calculation_trip_shop(fuel_price, shop)
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_cost}")
            list_cost.append(trip_cost)

        min_trip_cost = min(list_cost)
        best_shop = shops[list_cost.index(min_trip_cost)]
        if min_trip_cost >= customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")

        else:
            print(f"{customer.name} rides to {best_shop.name}\n")
            customer.trip_to_shop()
            customer.products_basket(best_shop)
            customer.go_to_home(min_trip_cost)


if __name__ == "__main__":
    shop_trip()
