from app.car import Car
from app.shop import Shop
from app.customer import Customer
import json


def shop_trip() -> None:
    with open("app/config.json", "r") as json_file:
        data_file = json.load(json_file)
        fuel_price = data_file["FUEL_PRICE"]
        shop_dict = {}
    for item in data_file["customers"]:
        customer = Customer(
            item["name"],
            item["product_cart"],
            item["location"],
            item["money"]
        )
        car = Car(item["car"]["brand"], item["car"]["fuel_consumption"])
        customer.customer_info()
        for shop_item in data_file["shops"]:
            shop = Shop(
                shop_item["name"],
                shop_item["location"],
                shop_item["products"]
            )
            fuel_cost = car.count_fuel_price(
                fuel_price, customer.location, shop.location
            )
            shopping_cost = shop.count_product_price(customer.product_cart)
            full_cost = round(fuel_cost * 2 + shopping_cost, 2)
            customer.shop_visit(shop.name, full_cost)
            shop_dict[full_cost] = shop
        nearest_shop = shop_dict[min(shop_dict.keys())]
        lowest_price = min(shop_dict.keys())
        if lowest_price <= customer.money:
            customer.change_location(nearest_shop.location)
            nearest_shop.print_bill(customer.name, customer.product_cart)
            customer.come_back_home(lowest_price)
            customer.change_location(item["location"])
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
