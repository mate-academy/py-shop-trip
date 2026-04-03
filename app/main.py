import json
import os
from app.shop import Shop
from app.customer import Customer


def shop_trip() -> None:
    base_path = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(base_path, "config.json")
    with open(config_path) as config_file:
        config = json.load(config_file)

    fuel_price = config["FUEL_PRICE"]
    shops = [
        Shop(shop["name"], shop["location"], shop["products"])
        for shop in config["shops"]
    ]
    customers = [Customer(person) for person in config["customers"]]

    for person in customers:
        print(f"{person.name} has {person.money} dollars")
        costs = person.calculate_total_costs(shops, fuel_price)

        cheapest_shop = None
        min_cost = float("inf")

        for shop, cost in costs:
            f_cost = f"{cost: g}".replace(" ", "")
            print(f"{person.name}'s trip to the {shop.name} costs {f_cost}")
            if cost < min_cost:
                min_cost = cost
                cheapest_shop = shop

        if person.money >= min_cost:
            print(f"{person.name} rides to {cheapest_shop.name}")
            person.go_to(cheapest_shop.location)

            cheapest_shop.print_receipt(person.name, person.product_cart)

            print(f"\n{person.name} rides home")
            person.return_home()

            person.money = round(person.money - min_cost, 2)
            f_money = f"{person.money: g}".replace(" ", "")
            print(f"{person.name} now has {f_money} dollars\n")
        else:
            print(
                f"{person.name} doesn't have enough money "
                "to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
