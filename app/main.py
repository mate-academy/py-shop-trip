import os
import json
from app.customer import Customer
from app.shop import Shop
from app.utils import distance, travel_cost


def print_not_enough_money(customer: any) -> None:
    print(
        f"{customer.name} "
        f"doesn't have enough money to make a purchase in any shop"
    )


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")
    with open(config_path) as f:
        config = json.load(f)

    config_fuel_cost = config["FUEL_PRICE"]

    customers = [Customer(**c) for c in config["customers"]]
    shops = [Shop(**s) for s in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        shop_costs = []

        for shop in shops:
            if all(item in shop.products for item in customer.product_cart):
                dist_to_shop = distance(customer.location, shop.location)
                dist_home = distance(shop.location, customer.location)
                fuel_cost = travel_cost(
                    dist_to_shop, customer.car, config_fuel_cost
                )
                return_cost = travel_cost(
                    dist_home, customer.car, config_fuel_cost
                )
                products_cost = sum(
                    shop.products[item] * qty
                    for item, qty in customer.product_cart.items()
                )
                total_cost = round(fuel_cost + return_cost + products_cost, 2)
                shop_costs.append(
                    (
                        total_cost,
                        shop,
                        fuel_cost,
                        return_cost,
                        products_cost
                    )
                )
                print(
                    f"{customer.name}'s "
                    f"trip to the {shop.name} costs {total_cost}")
            else:
                print(
                    f"{customer.name} "
                    f"cannot buy all products in {shop.name}"
                )
        if not shop_costs:
            print_not_enough_money(customer)
            continue

        shop_costs.sort(key=lambda x: x[0])
        (
            cheapest_total,
            chosen_shop,
            fuel_cost,
            return_cost,
            products_cost
        ) = shop_costs[0]

        if customer.money >= cheapest_total:
            print(f"{customer.name} rides to {chosen_shop.name}\n")

            chosen_shop.print_receipt(customer.name, customer.product_cart)
            customer.money = customer.money - cheapest_total

            print(f"{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars\n")
        else:
            print_not_enough_money(customer)


if __name__ == "__main__":
    shop_trip()
