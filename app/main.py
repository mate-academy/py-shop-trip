import json
import datetime
from app.customers import Customer
from app.shops import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    fuel_price = data["FUEL_PRICE"]
    customers = [Customer(**c) for c in data["customers"]]
    shops = [Shop(**s) for s in data["shops"]]

    for customer in customers:
        cost_to_road = customer.calculate_cost_to_road(shops, fuel_price)
        total_cost, min_cost_trip, chipest_shop_inst = customer.get_choice(
            shops, fuel_price
        )
        print(f"{customer.name} has {customer.money} dollars")
        for shop_name, road_cost in total_cost.items():
            print(
                f"{customer.name}'s trip to the "
                f"{shop_name} costs {round(total_cost[shop_name], 2)}"
            )
        if customer.money < min_cost_trip:
            print(
                f"{customer.name} doesn't have "
                f"enough money to make a purchase in any shop"
            )
            continue
        customer_cart = chipest_shop_inst.buy_products(customer)
        print(f"{customer.name} rides to {chipest_shop_inst.name}")
        home_location = customer.location
        customer.location = chipest_shop_inst.location
        print()
        print(
            f"Date: {datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
            f"Thanks, {customer.name}, for your purchase!"
        )
        print("You have bought:")
        for product_name, count_total_price in customer_cart.items():
            print(
                f"{count_total_price[0]} "
                f"{product_name}s for {count_total_price[1]} dollars"
            )
        print(
            f"Total cost is "
            f"{round(min_cost_trip - cost_to_road[chipest_shop_inst.name], 2)}"
            f" dollars"
        )
        print("See you again!\n")
        print(f"{customer.name} rides home")
        customer.location = home_location
        customer.money -= min_cost_trip
        print(f"{customer.name} now has {round(customer.money, 2)} dollars")
        print()


if __name__ == "__main__":
    shop_trip()
