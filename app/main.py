import json
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    info = {}
    with open("app/config.json", "r") as config:
        info = json.load(config)
    fuel_price = info["FUEL_PRICE"]
    customers = info["customers"]
    shops = info["shops"]
    dict_of_customers = {}
    dict_of_shops = {}
    for customer_data in customers:
        car = Car(customer_data["car"]["brand"],
                  customer_data["car"]["fuel_consumption"])
        dict_of_customers[customer_data["name"]] = Customer(
            customer_data["name"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["money"],
            car
        )
    for shop_data in shops:
        dict_of_shops[shop_data["name"]] = Shop(
            shop_data["name"],
            shop_data["products"],
            shop_data["location"]
        )
    for customer in dict_of_customers.values():
        print(f"{customer.name} has {customer.money} dollars")
        smaller_price = float("inf")
        smaller_shop = None
        for shop_name, shop in dict_of_shops.items():
            trip_price = customer.count_price_of_whole_trip(shop, fuel_price)
            print(f"{customer.name}'s trip to "
                  f"the {shop_name} costs {trip_price}")
            if trip_price < smaller_price:
                smaller_price = trip_price
                smaller_shop = shop_name
        if smaller_price < customer.money:
            customer.money -= smaller_price
            print(f"{customer.name} rides to {smaller_shop}\n")
            dict_of_shops[smaller_shop].return_receipt(customer.name,
                                                       customer.product_cart)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough"
                  f" money to make a purchase in any shop")
