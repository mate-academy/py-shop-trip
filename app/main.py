import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        dictionary = json.load(file)

    fuel_price = dictionary["FUEL_PRICE"]
    customers = [
        Customer.from_dict(customer)
        for customer in dictionary["customers"]
    ]
    shops = [Shop.from_dict(shop) for shop in dictionary["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        min_cost = None
        selected_shop = None
        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")

            if min_cost is None or min_cost > trip_cost:
                min_cost = trip_cost
                selected_shop = shop

        if min_cost > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            home_location = customer.location
            print(f"{customer.name} rides to {selected_shop.name}\n")
            customer.rides_to(selected_shop.location, fuel_price)

            selected_shop.process_purchase(customer)

            print(f"{customer.name} rides home")
            customer.rides_to(home_location, fuel_price)

            print(f"{customer.name} now has "
                  f"{round(customer.money, 2)} dollars\n")
