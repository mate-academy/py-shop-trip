import json
from app.shop import shop_list
from app.customer import Customer
from app.car import Car


def shop_trip() -> None:
    shops = shop_list

    with open("app/config.json", "r") as source:
        data = json.load(source)

    for person in data["customers"]:
        customer = Customer(person["name"],
                            person["product_cart"],
                            person["location"],
                            person["money"])
        car = Car(person["car"]["brand"],
                  person["car"]["fuel_consumption"],
                  data["FUEL_PRICE"])

        print(f"{customer.name} has {customer.money} dollars")
        choice = customer.analysis_of_shops(shops, car)
        if choice is None:
            return
        choice[0].get_receipt(customer, car)
        trip_costs = customer.trip_costs(choice[0], car)[1]
        print(f"{customer.name} rides home")
        money_left = round(customer.money - trip_costs, 2)
        print(f"{customer.name} now has {money_left} dollars\n")
