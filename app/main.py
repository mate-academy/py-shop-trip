import os
import json
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(current_dir, "config.json")

    with open(config_path, "r") as config_file:
        data = json.load(config_file)

    fuel_price = data["FUEL_PRICE"]

    shops = [Shop(shop_data) for shop_data in data["shops"]]
    customers = [
        Customer(**customer_data)
        for customer_data in data["customers"]
    ]

    for customer in customers:
        if customer != customers[0]:
            print()

        print(f"{customer.name} has {customer.money} dollars")

        shop_costs = {}

        for shop in shops:
            distance = customer.get_distance_to(shop.location)
            ride_cost = customer.get_ride_cost(distance, fuel_price)
            products_cost = shop.calculate_product_cost(
                customer.product_cart
            )

            total_cost = ride_cost + products_cost
            shop_costs[shop] = total_cost

            print(
                f"{customer.name}'s trip to the "
                f"{shop.name} costs {total_cost:.2f}"
            )

        cheapest_shop = min(shop_costs, key=shop_costs.get)
        cheapest_cost = shop_costs[cheapest_shop]

        if customer.money >= cheapest_cost:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = cheapest_shop.location

            final_products_cost = cheapest_shop.calculate_product_cost(
                customer.product_cart
            )

            cheapest_shop.print_receipt(
                customer_name=customer.name,
                product_cart=customer.product_cart,
                total_cost=final_products_cost
            )

            customer.money -= cheapest_cost

            print(f"\n{customer.name} rides home")
            print(f"{customer.name} now has {customer.money:.2f} dollars")
        else:
            print(
                f"{customer.name} doesn't have enough "
                "money to make a purchase in any shop"
            )


if __name__ == "__main__":
    shop_trip()
