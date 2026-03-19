import json

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
        trip_costs = []
        for shop in shops_dict.values():
            distance_there_and_back = customer.find_distance(shop.location)
            travel_cost = (
                customer.find_travel_cost(distance_there_and_back, fuel_price)
            )
            shopping_cost = shop.find_shopping_cost(customer)
            total_cost = round(travel_cost + shopping_cost, 2)
            print(
                f"{customer.name}'s trip "
                f"to the {shop.name} costs {total_cost}"
            )
            trip_costs.append((total_cost, shop))
        trip_costs.sort()
        lowest_price = trip_costs[0][0]
        cheapest_shop = trip_costs[0][1]
        if lowest_price > customer.money:
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
        else:
            print(f"{customer.name} rides to {cheapest_shop.name}\n")
            customer.location = cheapest_shop.location
            cheapest_shop.print_receipt(customer)
            print(f"{customer.name} rides home")
            customer.money = customer.money - lowest_price
            print(f"{customer.name} now has {customer.money} dollars")
        customer_count += 1
        if customer_count < len(customers_dict):
            print()
