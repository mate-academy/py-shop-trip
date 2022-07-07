import json
from app.customer import Customer
from app.shop import Shop


def shop_trip():
    with open("app/config.json", "r") as file:
        data = json.load(file)
    shops = []
    for shop in data["shops"]:
        shop_obj = Shop(shop["name"],
                        shop["location"],
                        shop["products"],
                        )
        shops.append(shop_obj)
    for customer in data["customers"]:
        customer_obj = Customer(customer["name"],
                                customer["product_cart"],
                                customer["location"],
                                customer["money"],
                                customer["car"]["fuel_consumption"])
        print(f"{customer_obj.name} has {customer_obj.money} dollars")
        cheapest_shop = shops[0]
        for shop in shops:
            cost_of_trip = shop.cost_of_trip(customer_obj, data['FUEL_PRICE'])
            print(f"{customer_obj.name}'s trip to the {shop.name}"
                  f" costs {cost_of_trip}")
            if shop < cheapest_shop:
                cheapest_shop = shop
        if customer_obj.money >= cheapest_shop.total_cost:
            print(f"{customer_obj.name} rides to {cheapest_shop.name}\n\n"
                  f"{cheapest_shop.receipt}\n\n"
                  f"{customer_obj.riding_home(cheapest_shop)}\n")
        else:
            print(f"{customer_obj.name}"
                  f" doesn't have enough money to make purchase in any shop")
