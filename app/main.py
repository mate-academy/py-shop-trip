import json

from math import dist

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:

    with open("config.json", "r") as file:
        data = json.load(file)

        fuel_price = data["FUEL_PRICE"]

        customers = [Customer(**customer) for customer in data["customers"]]
        shops = [Shop(**shop) for shop in data["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        car = Car(customer.car)
        shops_total = []

        for shop in shops:

            prod_cost = shop.calc_product_cost(customer.product_cart)
            distance = dist(customer.location, shop.location) * 2
            trip_cost = car.trip_cost(distance, fuel_price)
            total_cost = round(trip_cost + prod_cost, 2)

            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {total_cost}")

            if customer.money >= total_cost:
                shops_total.append((total_cost, shop))

        if not shops_total:
            print(f"{customer.name} doesn't have enough money "
                  f"to make purchase in any shop")
            break

        shops_total.sort()

        print(f"{customer.name} rides to {shops_total[0][1].name}\n")
        shops_total[0][1].print_check(customer.name, customer.product_cart)
        print(f"{customer.name} rides home")
        print(f"{customer.name} now has "
              f"{customer.money - shops_total[0][0]} dollars\n")


if __name__ == "__main__":
    shop_trip()
