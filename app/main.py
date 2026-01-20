import json
import os

from app.car import Car
from app.customer import Customer
from app.shop import Shop


def get_customers_from_dict(customers: dict) -> list[Customer]:
    result = []
    for customer in customers:
        result.append(Customer(
            customer["name"],
            customer["product_cart"],
            customer["location"],
            customer["money"],
            Car(
                customer["car"]["brand"],
                customer["car"]["fuel_consumption"]
            )
        ))
    return result


def get_shops_from_dict(shops: dict) -> list[Shop]:
    result = []
    for shop in shops:
        result.append(Shop(
            shop["name"],
            shop["location"],
            shop["products"]
        ))
    return result


def trip_to_shop(shop: Shop,
                 customer: Customer,
                 trip_cost: float) -> None:
    customer_location = customer.location
    print(f"{customer.name} rides to {shop.name}\n")
    customer.location = shop.location
    shop.serve_customer(customer)
    print(f"{customer.name} rides home")
    customer.location = customer_location
    customer.money -= trip_cost
    print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")


def shop_trip() -> None:
    directory = os.path.dirname(os.path.abspath(__file__))
    with open(f"{directory}/config.json", "r") as config:
        data = json.load(config)

    # Initialize data from dict
    fuel_price = data["FUEL_PRICE"]
    customers = get_customers_from_dict(data["customers"])
    shops = get_shops_from_dict(data["shops"])

    for customer_index, customer in enumerate(customers):
        print(f"{customer.name} has {customer.money} dollars")

        cheapest_shop = None
        cheapest_trip_cost = 0.0
        for shop in shops:
            trip_cost = (
                ((customer.calculate_distance(shop.location) / 100)
                 * customer.car.fuel_consumption) * fuel_price
            ) * 2

            for product, amount in customer.product_cart.items():
                if product in shop.products:
                    total_product_cost = shop.products[product] * amount
                    trip_cost += total_product_cost
                else:
                    continue

            if not cheapest_shop or cheapest_trip_cost > trip_cost:
                cheapest_shop = shop
                cheapest_trip_cost = trip_cost

            trip_cost = round(trip_cost, 2)
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs {trip_cost}")

        if not cheapest_shop or cheapest_trip_cost > customer.money:
            print(f"{customer.name} doesn't have "
                  f"enough money to make a purchase in any shop")
            if customer_index != len(customers) - 1:
                print("")
            continue

        trip_to_shop(cheapest_shop, customer, cheapest_trip_cost)


if __name__ == "__main__":
    shop_trip()
