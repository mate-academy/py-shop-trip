import json

from app.data.customers.customers import Customer
from app.data.shops.shops import Shop


def shop_trip() -> None:
    try:
        with open("app/config.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        raise Exception("File not found!")

    fuel_price = data["FUEL_PRICE"] / 100
    customers: list = [Customer(**cust) for cust in data["customers"]]
    shops: list = [Shop(**cust) for cust in data["shops"]]
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        cheapest_shop = None
        min_trip_cost = float("inf")

        for shop in shops:
            fuel_cost = round(customer.fuel_dist(shop)
                              * 2 * fuel_price, 2)
            total_trip_cost = shop.cost_in_store(customer, fuel_cost)

            if (total_trip_cost < min_trip_cost
                    and customer.money >= total_trip_cost):
                min_trip_cost = total_trip_cost
                cheapest_shop = shop

        if cheapest_shop:
            customer.money -= min_trip_cost
            customer.sales_receipt(cheapest_shop)
        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
