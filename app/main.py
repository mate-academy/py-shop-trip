import json

from app.shop_calculations import shopping
from app.shop import Shop
from app.customer import Customer
from app.shop_calculations import estimate_total_cost


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]

    customer_list = [
        Customer(customer["name"], customer["product_cart"],
                 customer["location"], customer["money"],
                 customer["car"]) for customer in customers]
    shop_list = [
        Shop(shop["name"], shop["location"],
             shop["products"]) for shop in shops]

    for customer in customer_list:
        print(f"{customer.name} has {customer.money} dollars")
        shop_cost_dict = {}
        for shop in shop_list:
            shop_cost = estimate_total_cost(fuel_price, customer, shop)
            shop_cost_dict[shop] = shop_cost
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {round(shop_cost, 2)}")

        chosen_shop = min(shop_cost_dict, key=shop_cost_dict.get)
        if customer.money >= shop_cost_dict[chosen_shop]:
            print(f"{customer.name} rides to {chosen_shop.name}")
            customer.location = chosen_shop.location
            shopping(customer, chosen_shop)
            print(f"{customer.name} rides home")
            money_last = round(
                (customer.money - shop_cost_dict[chosen_shop]), 2)
            print(f"{customer.name} now has {money_last} dollars")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")
