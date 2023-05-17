import json
from app.trip_elements.customer import Customer
from app.trip_elements.shop import Shop


def shop_trip() -> None:
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
            print(f"{customer.name}'s trip to"
                  f" the {shop.name} costs {trip_cost}")
        lowest_trip_cost = min(trip_costs.keys())
        if customer.money < lowest_trip_cost:
            print(f"{customer.name} doesn't have enough money"
                  f" to make a purchase in any shop")
            continue
        print(f"{customer.name} rides"
              f" to {trip_costs[lowest_trip_cost].name}\n")
        customer.money -= customer.car.gasoline_calculation(
            data["FUEL_PRICE"],
            customer.location,
            trip_costs[lowest_trip_cost].location
        )
        customer.location = trip_costs[lowest_trip_cost].location
        trip_costs[lowest_trip_cost].shop_visit(customer)
        print(f"{customer.name} rides home")
        customer.money -= customer.car.gasoline_calculation(
            data["FUEL_PRICE"],
            customer.location,
            customer.home_location
        )
        customer.location = customer.home_location
        print(f"{customer.name} now has {round(customer.money, 2)} dollars\n")
