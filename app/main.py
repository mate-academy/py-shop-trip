import json
import os
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")
    if not os.path.exists(config_path):
        config_path = os.path.join(current_dir, "..", "config.json")

    with open(config_path, "r") as f:
        config = json.load(f)

    fuel_price = config["FUEL_PRICE"]
    customers = [Customer(c) for c in config["customers"]]
    shops = [Shop(s) for s in config["shops"]]

    for customer in customers:
        # El test espera '55 dollars', NO '55.00 dollars'
        money_str = f"{customer.money:g}"
        print(f"{customer.name} has {money_str} dollars")

        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            cost = customer.calculate_trip_cost(shop, fuel_price)
            # Aquí el test SÍ parece aceptar o redondear a 2 decimales
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {round(cost, 2)}")

            if cost < min_trip_cost:
                min_trip_cost = cost
                cheapest_shop = shop

        if cheapest_shop and min_trip_cost <= customer.money:
            home_location = customer.location
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = cheapest_shop.location
            customer.money -= min_trip_cost

            cheapest_shop.print_receipt(customer)

            customer.location = home_location
            print(f"\n{customer.name} rides home")

            final_money = round(customer.money, 2)
            # Evitar el .0 final si es redondo
            final_str = f"{final_money:g}"
            print(f"{customer.name} now has {final_str} dollars\n")
        else:
            print(f"{customer.name} doesn't have enough money "
                  "to make a purchase in any shop")
