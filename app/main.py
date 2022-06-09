import json

from app.customer import Customer
from app.shop import Shop


FILE_NAME = "app/config.json"


def shop_trip():
    fuel_price, shops, customers = create_shops_and_customers(FILE_NAME)

    for customer in customers:
        chosen_shop, trip_costs = customer.get_customer_shop(shops, fuel_price)
        if chosen_shop is None:
            print(f"{customer.name} doesn't have enough "
                  f"money to make purchase in any shop")
        else:
            make_ride(customer, chosen_shop, trip_costs)


def create_shops_and_customers(file_name: str) -> tuple:
    with open(file_name) as file:
        config_data = json.load(file)

    fuel_price = config_data["FUEL_PRICE"]
    shops = [
        Shop(shop_data)
        for shop_data in config_data["shops"]
    ]
    customers = [
        Customer(user_data)
        for user_data in config_data["customers"]
    ]

    return fuel_price, shops, customers


def make_ride(customer: Customer, shop: Shop, trip_costs: float):
    print(f"{customer.name} rides to {shop.name}\n")
    customer.ride_to_shop(shop)
    shop.sell_products(customer)
    print(f"{customer.name} rides home")
    customer.pay_for_trip(trip_costs)
    customer.ride_to_home()
    print(f'{customer.name} now has {customer.money} dollars\n')
