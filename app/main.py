import json
import datetime

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        shopping_data = json.load(file)
    fuel_price = shopping_data["FUEL_PRICE"]
    customers_dict = {}
    shops_dict = {}
    for customer in shopping_data["customers"]:
        customers_dict[customer["name"]] = Customer(customer)
    for shop in shopping_data["shops"]:
        shops_dict[shop["name"]] = Shop(shop)
    customer_count = 0
    for customer in customers_dict.values():
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}
        for shop in shops_dict.values():
            distance_there_and_back = (
                2 * (
                    (customer.location[0] - shop.location[0]) ** 2
                    + (customer.location[1] - shop.location[1]) ** 2
                ) ** 0.5
            )
            travel_cost = (
                distance_there_and_back * fuel_price
                * customer.car.fuel_consumption / 100
            )
            shopping_cost = sum(
                customer.product_cart[product] * shop.products[product]
                for product in customer.product_cart
            )
            total_cost = round(travel_cost + shopping_cost, 2)
            print(
                f"{customer.name}'s trip "
                f"to the {shop.name} costs {total_cost}"
            )
            trip_costs[total_cost] = [shop, shopping_cost]
        lowest_price = min(trip_cost for trip_cost in trip_costs)
        cheapest_shop = trip_costs[lowest_price][0]
        shopping_cost = trip_costs[lowest_price][1]
        if lowest_price > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = cheapest_shop.location
            print(
                f"Date: "
                f"{datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')}\n"
                f"Thanks, {customer.name}, for your purchase!\n"
                f"You have bought:"
            )
            for key, value in customer.product_cart.items():
                product_cost = value * cheapest_shop.products[key]
                if product_cost % 1 == 0:
                    product_cost = int(product_cost)
                print(
                    f"{value} {key}s for "
                    f"{product_cost} dollars"
                )
            print(
                f"Total cost is {shopping_cost} dollars\n"
                f"See you again!\n\n"
                f"{customer.name} rides home"
            )
            customer.money = customer.money - lowest_price
            print(f"{customer.name} now has {customer.money} dollars")
        customer_count += 1
        if customer_count < len(customers_dict):
            print()
