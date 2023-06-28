import datetime
import json

from app.customer import Customer
from app.shop import Shop


def shop_trip() -> None:
    with open("app/config.json", "r") as f:
        config = json.load(f)
        fuel_price = config["FUEL_PRICE"]
        customers = [Customer(customer["name"],
                              customer["product_cart"],
                              customer["location"],
                              customer["money"],
                              customer["car"])
                     for customer in config["customers"]]
        shops = [Shop(shop["name"],
                      shop["location"],
                      shop["products"])
                 for shop in config["shops"]]

    for customer in customers:
        print(f"{customer.name} has {customer.money} dollars")
        trip_cost_dict = {}
        for shop in shops:
            fuel_cost = (customer.distance(shop) / 100
                         * customer.car.get("fuel_consumption")
                         * fuel_price)
            trip_cost = fuel_cost * 2 + customer.products_cost(shop)
            trip_cost_dict[trip_cost] = shop
            print(f"{customer.name}'s trip to the "
                  f"{shop.name} costs "
                  f"{round(trip_cost, 2)}")
        cheapest_trip = min(trip_cost_dict)
        optimal_shop = trip_cost_dict[cheapest_trip]
        if cheapest_trip > customer.money:
            print(f"{customer.name} doesn't have enough money "
                  f"to make a purchase in any shop")
        else:
            print(f"{customer.name} rides to {optimal_shop.name}" + "\n")
            print(datetime.datetime.now().strftime("Date: %d/%m/%Y %H:%M:%S"))
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought: ")
            total_cost = 0
            for product, quantity in customer.product_cart.items():
                product_price = quantity * optimal_shop.products[product]
                total_cost += product_price
                print(f"{quantity} {product}s for {product_price} dollars")
            print(f"Total cost is {total_cost} dollars")
            print("See you again!" + "\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} now has "
                  f"{round(customer.money - cheapest_trip, 2)} dollars" + "\n")
