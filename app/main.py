from json import load

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip():

    with open("app/config.json", "r") as f:
        data = load(f)

    # creating variables from loaded data
    fuel_price = data["FUEL_PRICE"]
    customers = []
    for customer in data["customers"]:
        car = Car(**customer["car"])
        customers.append(Customer(customer["name"], customer["product_cart"],
                                  customer["location"], customer["money"],
                                  car))
    shops = [Shop(**shop) for shop in data["shops"]]

    # performing purchase calculations
    for ind, customer in enumerate(customers):
        if ind <= len(customers):
            customer.perform_purchase(shops, fuel_price)
