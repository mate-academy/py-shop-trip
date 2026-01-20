import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as config_file:
        data = json.load(config_file)
        customers = data["customers"]
        shops = data["shops"]

    for person in customers:
        customer = Customer(
            person["name"],
            person["product_cart"],
            person["location"],
            person["money"],
        )
        car = Car(person["car"]["brand"], person["car"]["fuel_consumption"])
        print(customer)

        cost_options = {}
        for shop in shops:
            shop_inst = Shop(
                shop["name"],
                shop["location"],
                shop["products"]
            )
            distance = shop_inst.calculate_trip_distance(customer)
            fuel_cost = (data["FUEL_PRICE"] * car.litres_per_trip(distance))
            total = round(
                fuel_cost * 2 + shop_inst.shopping_cost(customer),
                2
            )
            cost_options[total] = shop_inst
            print(f"{customer.name}'s trip to the "
                  f"{shop_inst.name} costs {total}")

        if customer.money >= min(cost_options):
            cheapest_shop = cost_options[min(cost_options)]
            print(f"{customer.name} rides to {cheapest_shop.name}")
            customer.location = cheapest_shop.location
            customer.money -= min(cost_options)
            cheapest_shop.issue_receipt(customer)
            print(
                f"\n{customer.name} rides home\n"
                f"{customer.name} now has {customer.money} dollars\n"
            )
        else:
            print(f"{customer.name} "
                  f"doesn't have enough money to make a purchase in any shop")


shop_trip()
