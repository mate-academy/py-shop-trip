import json
import os

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(os.path.join("app", "config.json"), "r") as f:
        all_data = json.load(f)

    customers_data = all_data["customers"]
    shops_list = [
        Shop(shop["name"], shop["products"], shop["location"])
        for shop in all_data["shops"]
    ]
    fuel_price = all_data["FUEL_PRICE"]
    for customer_data in customers_data:
        current_customer = Customer(
            customer_data["name"],
            customer_data["money"],
            customer_data["product_cart"],
            customer_data["location"],
            customer_data["car"],
        )

        print(f"{current_customer.name} has {current_customer.money} dollars")

        chosen_shop = current_customer.choose_shop(shops_list, fuel_price)
        if not isinstance(chosen_shop, Shop):
            print(
                f"{current_customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
            continue
        print(f"{current_customer.name} rides to {chosen_shop.name}\n")
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {current_customer.name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for quant, item in current_customer.product_cart.items():
            curr_cost = chosen_shop.product_price.get(quant, 0) * item
            if curr_cost == int(curr_cost):
                curr_cost = int(curr_cost)
            total_cost += curr_cost
            print(f"{item} {quant}s for {curr_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!\n")
        print(f"{current_customer.name} rides home")
        print(
            f"{current_customer.name} now has"
            f" {current_customer.money} dollars\n"
        )


if __name__ == "__main__":
    shop_trip()
