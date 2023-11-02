import json
import os
import datetime

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open(os.path.join("app", "config.json"), "r") as f:
        all_data = json.load(f)

    customers_data = all_data["customers"]
    shops_list = [
        Shop(**shop)
        for shop in all_data["shops"]
    ]
    fuel_price = all_data["FUEL_PRICE"]
    for customer_data in customers_data:
        current_customer = Customer(**customer_data)

        now = datetime.datetime.now()
        formatted_date = now.strftime("%d/%m/%Y %H:%M:%S")

        print(f"{current_customer.name} has {current_customer.money} dollars")

        chosen_shop = current_customer.choose_shop(shops_list, fuel_price)
        if not isinstance(chosen_shop, Shop):
            print(
                f"{current_customer.name} doesn't have enough money"
                f" to make a purchase in any shop"
            )
            continue
        print(
            f"{current_customer.name} rides to {chosen_shop.name}\n"
            f"\nDate: {formatted_date}\n"
            f"Thanks, {current_customer.name}, for your purchase!\n"
            "You have bought: "
        )
        total_cost = 0
        for quant, item in current_customer.product_cart.items():
            curr_cost = chosen_shop.products.get(quant, 0) * item
            if curr_cost == int(curr_cost):
                curr_cost = int(curr_cost)
            total_cost += curr_cost
            print(f"{item} {quant}s for {curr_cost} dollars")

        print(
            f"Total cost is {total_cost} dollars\n"
            "See you again!\n"
            f"\n{current_customer.name} rides home\n"
            f"{current_customer.name} now has "
            f"{current_customer.money} dollars\n"
        )


if __name__ == "__main__":
    shop_trip()
