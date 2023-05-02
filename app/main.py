import math
from app.customer import customers_list
from app.shop import shops_list


def shop_trip() -> None:
    for customer in customers_list:
        print(f"{customer.name} has {customer.money} dollars")
        cost_trip = {}
        for shop in shops_list:
            distance = math.dist(customer.location, shop.location)

            cost_trip[shop] = round(
                customer.cost_trip(distance) + customer.sum_products(
                    shop.products), 2)
            print(
                f"{customer.name}'s trip to the {shop.name} costs "
                f"{cost_trip[shop]}")

        if customer.money > min(cost_trip.values()):
            cheaper_shop = min(cost_trip, key=cost_trip.get)
            print(f"{customer.name} rides to {cheaper_shop.name}\n")

            total_spend = cheaper_shop.receipt(customer)
            print(f"Total cost is {total_spend} dollars\nSee you again!")
            print()
            print(f"{customer.name} rides home"
                  f"\n{customer.name} now has "
                  f"{customer.money - cost_trip[cheaper_shop]} dollars")
            print()

        else:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")


shop_trip()
