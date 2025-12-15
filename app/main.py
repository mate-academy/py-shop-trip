import json

from app.gas_station import GasStation
from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        date = json.load(file)
        gas_station = GasStation(date["FUEL_PRICE"])
        customers_date = date["customers"]
        shops_date = date["shops"]

    for customer in customers_date:
        customer = Customer(
            name=customer["name"],
            product_cart=customer["product_cart"],
            location=customer["location"],
            money=customer["money"],
            car=Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        )
        print(f"{customer.name} has {customer.money} dollars")

        # Calculate the cost of the trip to each shop
        costs = {}
        for shop in shops_date:
            shop = Shop(**shop)
            cost = customer.costs_for_trip_to_shop(shop, gas_station.price)
            costs[cost] = shop
            print(f"{customer}'s trip to the {shop} costs {cost}")

        if not customer.enough_money(min(costs)):
            break
        cheapest_shop = costs[min(costs)]
        print(
            f"{customer} rides to {cheapest_shop}\n\n"
            f"Date: 04/01/2021 12:33:41\n"
            f"Thanks, {customer}, for your purchase!\n"
            f"{customer.get_receipts(cheapest_shop)}\n\n"
            f"{customer} rides home\n"
            f"{customer} now has "
            f"{customer.calculate_wallet(min(costs))} dollars\n"
        )


if __name__ == "__main__":
    shop_trip()
