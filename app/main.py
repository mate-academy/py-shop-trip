import json
import os


from app.customer import Customer
from app.shop import Shop

BASE_DIR = os.path.dirname(os.path.realpath(__file__))


def shop_trip() -> None:
    with open(f"{BASE_DIR}/config.json") as file_data:
        data = json.load(file_data)
    fuel_price = data["FUEL_PRICE"]
    customers = Customer.json_list_to_customer_objects(data["customers"])
    shops = Shop.json_list_to_shop_objects(data["shops"])

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_to_shop_costs = customer.find_full_cost_of_travel(
            shops, fuel_price
        )
        suitable_shop, price = customer.find_cheapest_trip(trip_to_shop_costs)

        if price > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
            return
        customer.print_customer_purchase(suitable_shop)
        customer.money -= price
        print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
