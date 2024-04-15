import json
from app.customer import Customer
from app.car import Car
from app.shop import Shop


def shop_trip() -> None:

    with open("app/config.json", "r") as config:
        config_dict = json.load(config)
        fuel_cost = config_dict["FUEL_PRICE"]
        customers_list = []
        for customer in config_dict["customers"]:
            person = Customer(customer["name"],
                              customer["product_cart"],
                              customer["location"],
                              customer["money"],
                              Car(*customer["car"].values()))
            customers_list.append(person)
        shops_list = [Shop(*shop.values()) for shop in config_dict["shops"]]

    for customer in customers_list:
        customer.money_available()
        home = customer.location
        min_cost = min(customer.trip_costing(shops_list, fuel_cost),
                       key=lambda x: x[2])
        if min_cost[2] <= customer.money:
            print(f"{customer.name} rides to {min_cost[1]}\n")
            customer.location = min_cost[0].location
            min_cost[0].print_check(customer.name, customer.product_cart)
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money - min_cost[2], 2)} dollars\n")
            customer.location = home
        else:
            print(f"{customer.name} doesn't have enough "
                  f"money to make a purchase in any shop")


if __name__ == "__main__":
    shop_trip()
