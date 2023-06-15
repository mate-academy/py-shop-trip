import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)
        customers_data = data["customers"]
        fuel_price = data["FUEL_PRICE"]
        shops_data = data["shops"]

    customers_objs = Customer.from_dict(customers_data)
    shops_objs = Shop.from_dict(shops_data)
    for customer in customers_objs:
        Customer.print_header(customer)
        shops_price = []
        for shop in shops_objs:
            trip_data = Customer.print_trip_cost(customer, shop, fuel_price)
            shops_price.append(trip_data)
            shops_price.sort(key=lambda x: x.get("total"))
        Customer.check_money_for_trip(customer, shops_price[0])
