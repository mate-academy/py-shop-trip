import json

from app.car import GetCarsData
from app.customer import GetCustomersData
from app.shop import GetShopsData


def shop_trip() -> None:
    with open("app.config.json", "r") as f:
        all_data = json.load(f)

    customers_data = all_data["customers"]
    shops_list = [GetShopsData(shop) for shop in all_data["shops"]]
    fuel_price = all_data["FUEL_PRICE"]
    for customer in customers_data:
        current_customer = GetCustomersData(customer)
        current_car = GetCarsData(customer)

        print(f"{current_customer.name} has {current_customer.money} dollars")

        chosen_shop = current_customer.choose_shop(
            shops_list, current_car, fuel_price
        )
        if not isinstance(chosen_shop, GetShopsData):
            print((f"{current_customer.name} doesn't have "
                   f"enough money to make a purchase in any shop"))
            continue
        print(f"{current_customer.name} rides to {chosen_shop.name}")
        print()
        print("Date: 04/01/2021 12:33:41")
        print(f"Thanks, {current_customer.name}, for your purchase!")
        print("You have bought: ")
        total_cost = 0
        for quant, item in current_customer.product_cart.items():
            curr_cost = chosen_shop.product_price.get(quant) * item
            curr_cost = int(curr_cost) if \
                int(curr_cost) == curr_cost \
                else curr_cost
            total_cost += curr_cost
            print(f"{item} {quant}s for {curr_cost} dollars")
        print(f"Total cost is {total_cost} dollars")
        print("See you again!")
        print()
        print(f"{current_customer.name} rides home")
        print((f"{current_customer.name} now "
               f"has {current_customer.money} dollars"))
        print()
