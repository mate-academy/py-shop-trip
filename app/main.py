from _datetime import datetime
import json

from app.trips_cost import calculate_trips_cost, Shop


def shop_trip() -> None:
    with open("config.json", "r") as file:
        config = json.load(file)
        fuel_price = config["FUEL_PRICE"]
        customers = config["customers"]
        shops_config = config["shops"]
        shops = [
            Shop(shop["name"], shop["location"], shop["products"])
            for shop in shops_config
        ]
        for customer in customers:
            cheapest_cost, cheapest_shop, rest_of_money = calculate_trips_cost(
                customer, shops, fuel_price
            )
            if rest_of_money >= 0:
                print(f"{customer['name']} rides to {cheapest_shop[0]}")
                date = datetime(2021, 4, 1, 12, 33, 41)
                print(f"\nDate: {date.strftime('%m/%d/%Y %H:%M:%S')}\n"
                      f"Thanks, {customer['name']}, for you purchase!\n"
                      f"You have bought: ")
                total_cost = 0
                for product, price in cheapest_shop[1].items():
                    print(f"{product[1]} {product[0]}s for {price} dollars")
                    total_cost += price
                print(f"Total cost is {total_cost} dollars\n"
                      f"See you again!\n"
                      f"\n{customer['name']} rides home\n"
                      f"{customer['name']} now has {rest_of_money} dollars\n")
            else:
                print(f"{customer['name']} doesn't have enough money "
                      f"to make purchase in any shop")


if __name__ == "__main__":
    shop_trip()
