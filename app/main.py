import json

from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        info = json.load(file)

        fuel_price = info["FUEL_PRICE"]
        customers_data = info["customers"]
        shops_data = info["shops"]

    customers = Customer.make_customers(customers_data)
    shops = Shop.make_shops(shops_data)

    for customer in customers:
        home_location = customer.location

        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop, min_trip_cost = customer.find_cheapest_shop(
            shops,
            fuel_price
        )

        if cheapest_shop:
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.location
            cheapest_shop.make_purchase(customer)
            customer.money -= min_trip_cost
            print(f"{customer.name} rides home")
            customer.location = home_location
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
