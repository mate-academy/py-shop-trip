import json

from app.car import Car
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:

    with open("app/config.json", "r") as json_file:
        data = json.load(json_file)
        fuel_price = data.get("FUEL_PRICE")
        shops = {}

    for client in data.get("customers"):
        customer = Customer(
            client.get("name"),
            client.get("product_cart"),
            client.get("location"),
            client.get("money"),
        )
        car_dict = client.get("car")
        car = Car(car_dict.get("brand"), car_dict.get("fuel_consumption"))
        customer.customer_information()

        for shop_item in data.get("shops"):
            shop = Shop(
                shop_item.get("name"),
                shop_item.get("location"),
                shop_item.get("products"),
            )
            fuel_cost = car.count_fuel_price(
                fuel_price,
                customer.location,
                shop.location
            )
            shopping_cost = shop.calculate_product_price(customer.product_cart)
            full_cost = round(fuel_cost * 2 + shopping_cost, 2)
            customer.shop_visit(shop.name, full_cost)
            shops[full_cost] = shop

        nearest_shop = shops[min(shops.keys())]
        lowest_price = min(shops.keys())

        if lowest_price <= customer.money:
            customer.change_location(nearest_shop.location)
            nearest_shop.print_check(customer.name, customer.product_cart)
            customer.return_home(lowest_price)
            customer.change_location(client.get("location"))
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")
