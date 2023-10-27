import json

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def create_customers_list(customers: dict):
    result = []
    for customer in customers:
        current_car = Car(customer["car"]["brand"],
                          customer["car"]["fuel_consumption"])

        current_customer = Customer(customer["name"],
                                    customer["product_cart"],
                                    customer["location"],
                                    customer["money"],
                                    current_car)
        result.append(current_customer)

    return result


def create_shops_list(shops: dict):
    result = []
    for shop in shops:
        current_shop = Shop(shop["name"],
                            shop["location"],
                            shop["products"])
        result.append(current_shop)

    return result


def shop_visit(customer: Customer, shop: Shop, fuel_price):
    home_location = (customer.location_x, customer.location_y)
    trip_price = customer.count_trip_price(shop, fuel_price)

    customer.change_location(shop.location_x, shop.location_y)
    customer.pay(trip_price)

    shop.give_check(customer.name, customer.product_cart)
    purchase_price = customer.count_purchase_price(shop)
    customer.pay(purchase_price)

    customer.pay(trip_price)
    customer.go_home()
    customer.change_location(home_location[0], home_location[1])


def shop_trip():
    with open("app/config.json", "r") as file_data:
        file_data = json.load(file_data)

        fuel_price = file_data["FUEL_PRICE"]
        customers_list = create_customers_list(file_data["customers"])
        shops_list = create_shops_list(file_data["shops"])

    for current_customer in customers_list:
        current_shop = current_customer.choose_cheapest_trip(shops_list,
                                                             fuel_price)
        if current_shop is not None:
            shop_visit(current_customer, current_shop, fuel_price)


shop_trip()
