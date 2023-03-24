from customer import Customer
from shop import Shop
import json
from datetime import datetime


def load_config():
    with open('config.json', 'r') as file:
        config = json.load(file)
    return config


def shop_trip():
    global fuel_cost
    config = load_config()

    FUEL_PRICE = config['FUEL_PRICE']
    customers = [Customer(**customer_data) for customer_data in config['customers']]
    shops = [Shop(**shop_data) for shop_data in config['shops']]

    for customer in customers:
        min_cost = float('inf')
        selected_shop = None

        for shop in shops:
            trip_distance = customer.distance_to(shop.location) * 2
            fuel_cost = customer.car.trip_cost(trip_distance, FUEL_PRICE)

            product_cost = customer.calculate_product_cost(shop)

            total_cost = fuel_cost + product_cost

            if total_cost < min_cost:
                min_cost = total_cost
                selected_shop = shop

        if customer.money >= min_cost:
            customer.go_to_shop(selected_shop, min_cost)
            print_purchase_receipt(customer, selected_shop, min_cost, fuel_cost)
            customer.go_home()
        else:
            print(f"{customer.name} couldn't afford the trip to {selected_shop.name} (${min_cost:.2f}).\n")


def print_purchase_receipt(customer, shop, total_cost, fuel_cost):
    print(f"{customer.name} went to {shop.name} and spent ${total_cost:.2f}.")
    print(f"Purchase receipt at {datetime.now().strftime('%m/%d/%Y %H:%M:%S')}:")
    customer.print_product_receipt(shop)
    print(f"Fuel cost: ${fuel_cost:.2f}\n")
