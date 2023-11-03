import os.path
import json
from pathlib import Path


from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    file_path = os.path.join(Path(__file__).parent, "config.json")
    with open(file_path, "r") as file:
        json_data = json.load(file)

    fuel_price = json_data["FUEL_PRICE"]

    customers = [
        Customer(
            **customer
        ) for customer in json_data["customers"]
    ]
    shops = [
        Shop(
            **shop
        ) for shop in json_data["shops"]
    ]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")

        possible_shops = customer.calculate_total_trip_cost_for_each_shop(
            shops, fuel_price
        )

        for shop in shops:
            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {possible_shops[shop]}")

        cheapest_shop = customer.choose_cheapest_shop()

        if cheapest_shop["total_cost"] <= customer.money:
            customer.go_to_the_shop()
            shop = cheapest_shop["shop"]
            print(f"{customer.name} rides to {shop.name}"
                  "\n")

            shop.print_purchase_receipt(customer)

            customer.go_home()
            print(f"{customer.name} rides home")

            rest_of_money = customer.calculate_rest_of_money()
            print(f"{customer.name} now has {rest_of_money} dollars"
                  "\n")

        else:
            print(f"{customer.name} doesn't have enough "
                  "money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
