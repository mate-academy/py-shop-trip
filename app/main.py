from models import Customer, Shop
from helpers import load_config


def shop_trip():
    config = load_config()
    fuel_price = config["FUEL_PRICE"]

    shops = [Shop(s["name"], s["location"], s["products"]) for s in config["shops"]]
    customers = [Customer(c) for c in config["customers"]]

    for person in customers:
        print(f"{person.name} has {person.money} dollars")

        best_shop = None
        min_cost = float('inf')
        best_costs_details = None

        for shop in shops:
            costs = person.calculate_trip_costs(shop, fuel_price)
            print(f"{person.name}'s trip to the {shop.name} costs {costs['total']:.2f}")

            if costs["total"] < min_cost:
                min_cost = costs["total"]
                best_shop = shop
                best_costs_details = costs

        if best_shop and person.money >= min_cost:
            print(f"{person.name} rides to {best_shop.name}\n")

            person.location = best_shop.location

            person.print_receipt(best_shop, best_costs_details)

            print(f"\n{person.name} rides home")
            person.location = config["customers"][0]["location"]
            person.money -= min_cost
            print(f"{person.name} now has {person.money:.2f} dollars\n")
        else:
            print(f"{person.name} doesn't have enough money to make a purchase in any shop\n")


if __name__ == "__main__":
    shop_trip()
