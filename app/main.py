import os
import json
from .customer import Customer
from .shop import Shop


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")

    try:
        with open(config_path, "r") as f:
            config = json.load(f)
    except FileNotFoundError:
        print(f"Error path {config_path}")
        return

    fuel_price: float = config["FUEL_PRICE"]
    shops: list[Shop] = [
        Shop(s["name"], s["location"], s["products"]) for s in config["shops"]
    ]
    customers: list[Customer] = [Customer(c) for c in config["customers"]]

    for person in customers:
        print(f"{person.name} has {person.money} dollars")

        home_location = person.location
        best_shop = None
        min_trip_cost = float("inf")

        # 1. Аналізуємо ціни
        for shop in shops:
            cost = person.get_trip_cost(shop, fuel_price)
            print(f"{person.name}'s trip to the {shop.name} costs {cost:.2f}")

            if cost < min_trip_cost:
                min_trip_cost = cost
                best_shop = shop

        # 2. Перевіряємо, чи вистачає грошей
        if best_shop and person.money >= min_trip_cost:
            print(f"{person.name} rides to {best_shop.name}\n")

            person.drive_to(best_shop.location)

            best_shop.print_receipt(person.name, person.product_cart)

            print(f"\n{person.name} rides home")
            person.drive_to(home_location)

            # залишок грошей
            person.money -= min_trip_cost
            print(f"{person.name} now has {person.money:.2f} dollars\n")
        else:
            print(
                f"{person.name} doesn't have "
                f"enough money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
