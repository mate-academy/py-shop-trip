import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        data = json.load(file)

    Customer.generate_unit(data)
    Shop.generate_shop(data)

    for customer in Customer.group_customers:
        print(f"{customer.name} has {customer.money} dollars")

        best_shop, trip_cost = None, float("inf")

        for shop in Shop.shop_list:
            trip_calculate = customer.calculate_cost(shop, data)
            if trip_calculate < trip_cost:
                trip_cost = trip_calculate
                best_shop = shop

            print(f"{customer.name}'s trip to the {shop.name} "
                  f"costs {trip_calculate}")

        money_change = customer.money - trip_cost
        if money_change < 0:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop"
                  )
            return

        print(f"{customer.name} rides to {best_shop.name}")

        best_shop.get_service(customer)

        print(f"{customer.name} rides home")
        print(f"{customer.name} now has {round(money_change, 2)} dollars\n")


if __name__ == "__main__":
    shop_trip()
