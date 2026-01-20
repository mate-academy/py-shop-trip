import json

from app.additional_funcs import (create_instances,
                                  total_trip_cost,
                                  customer_can_go_to_shop,
                                  print_shop_receipt,
                                  taking_back_home)


def shop_trip() -> None:
    with open("app/config.json", "r") as c:
        config = json.load(c)
    fuel_price = config["FUEL_PRICE"]
    customers = config["customers"]
    shops = config["shops"]
    customers_list, shops_list = create_instances(customers, shops)
    total_trip_cost(fuel_price, customers_list, shops_list)
    for customer in customers_list:
        trip_to_shop = (customer_can_go_to_shop(customer))
        if customer.money >= min(customer.trips_costs.values()):
            print_shop_receipt(
                customer,
                shops_list,
                trip_to_shop)
            taking_back_home(customer, min(customer.trips_costs.values()))
