import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]
    customers_data = config["customers"]
    shops_data = config["shops"]

    customers = [Customer(**customer_data) for customer_data in customers_data]
    shops = [Shop(**shop_data) for shop_data in shops_data]

    for customer in customers:
        cheapest_shop = None
        min_cost = float("inf")
        shops_distans = {}

        for shop in shops:
            trip_cost = customer.calculate_trip_cost(shop, fuel_price)
            shops_distans[shop] = trip_cost
            min_cost = min(shops_distans.values())
            cheapest_shop = min(shops_distans, key=shops_distans.get)

        if shops_distans:
            print(f"{customer.name} has {customer.money} dollars")
            for name in shops_distans:
                print(f"{customer.name}'s trip to "
                      f"the {name.name} costs {shops_distans[name]}")

        if customer.money >= min_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.update_location(cheapest_shop.location)
            cheapest_shop.print_purchase_receipt(customer)
            print(f"{customer.name} now has "
                  f"{customer.money - min_cost} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


shop_trip()
