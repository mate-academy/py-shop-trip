import json

from app.Calculate_modules.best_price_shop import best_price_shop
from app.Calculate_modules.calculate_trip import calculate_trip
from app.Calculate_modules.going_to_shop import going_to_shop
from datetime import datetime
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        dict1 = json.load(file)

    customers = []
    for customer in dict1["customers"]:
        customer["car"] = Car(**customer["car"])
        customer["home_location"] = customer["location"]
        customers.append(Customer(**customer))

    shops = [Shop(**shop) for shop in dict1["shops"]]

    fuel_price = dict1["FUEL_PRICE"]

    calculate_trip(customers, shops, fuel_price)
    best_price_shop(customers)

    for customer in customers:
        going_to_shop(customer, shops)
        if customer.cheapest_cost < customer.money:
            print(f"\nDate: {datetime.now().replace(microsecond=0)}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")
            for shop_name, products in customer.price_of_products.items():
                if shop_name == customer.cheapest_shop:
                    for prod, price in products.items():
                        for prod2, number in customer.product_cart.items():
                            if prod == prod2:
                                print(f"{number} {prod2}(s) for "
                                      f"{round(float(price), 2)}")
            for key, value in customer.total_price.items():
                if key == customer.cheapest_shop:
                    print(f"Total cost is {round(float(value), 2)} dollars")
            print("See you again!")
            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round((float(customer.money)
                            - float(customer.cheapest_cost)), 2)}"
                  f" dollars")

    for customer in customers:
        customer.location = customer.home_location
