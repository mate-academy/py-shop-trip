import json
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json") as file:
        config = json.load(file)

    fuel_price = config["FUEL_PRICE"]

    customers = [
        Customer(
            config_customer["name"],
            config_customer["product_cart"],
            config_customer["location"],
            config_customer["money"],
            Car(**config_customer["car"])
        )
        for config_customer in config["customers"]
    ]

    shops = [Shop(**config_shop) for config_shop in config["shops"]]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trips = []

        for shop in shops:
            distance_to_shop = customer.distance_to(shop.location)
            cost_to_shop = customer.travel_cost(distance_to_shop, fuel_price)
            purchase_cost = customer.purchase_cost(shop.products)
            total_trip_cost = 2 * cost_to_shop + purchase_cost
            trips.append((total_trip_cost, shop))

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs{total_trip_cost: .2f}")

        trips.sort(key=lambda x: x[0])
        cheapest_trip = trips[0]
        total_cost, chosen_shop = cheapest_trip

        if total_cost <= customer.money:
            print(f"{customer.name} rides to {chosen_shop.name}\n")
            customer.print_receipt(chosen_shop.name, chosen_shop.products)
            customer.money -= total_cost
            print(f"{customer.name} rides home\n"
                  f"{customer.name} now has{customer.money: .2f} dollars\n")

    print(f"{customer.name} doesn't have enough money "
          f"to make a purchase in any shop")
