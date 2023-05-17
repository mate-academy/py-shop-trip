import json
from app.trip_elements.customer import Customer
from app.trip_elements.shop import Shop


def shop_trip():
    with open("app/config.json", "r") as config:
        data = json.load(config)
    customers = []
    shops = []
    for customer in data["customers"]:
        customers.append(Customer(customer))
    for shop in data["shops"]:
        shops.append(Shop(shop))
    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_costs = {}
        for shop in shops:
            trip_cost = shop.total_trip_cost(data["FUEL_PRICE"], customer)
            trip_costs[trip_cost] = shop
            print(f"{customer.name}'s trip to the {shop.name} costs {trip_cost}")
        lowest_trip_cost = min(trip_costs.keys())
        if customer.money < lowest_trip_cost:
            print(f"{customer.name} doesn't have enough money to make a purchase in any shop")
            continue
        print(f"{customer.name} rides to {trip_costs[lowest_trip_cost].name}\n")
        customer.money -= customer.car.gasoline_cost_calculation(data["FUEL_PRICE"],
                                                                 customer.location,
                                                                 trip_costs[lowest_trip_cost].location)
        customer.location = trip_costs[lowest_trip_cost].location
        trip_costs[lowest_trip_cost].shop_visit(customer)
        print(f"{customer.name} rides home")
        customer.money -= customer.car.gasoline_cost_calculation(data["FUEL_PRICE"],
                                                                 customer.location,
                                                                 customer.home_location)
        customer.location = customer.home_location
        print(f"{customer.name} now has {customer.money} dollars\n")

shop_trip()