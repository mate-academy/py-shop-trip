import json
import datetime
from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with (open("config.json", "r") as file):
        # load file into dictionary
        shopping_dict = json.load(file)
        fuel_price = shopping_dict["FUEL_PRICE"]

        # list of just customers
        customer_list = shopping_dict["customers"]
        # list of just shops as Shop instances
        shop_list = [Shop(shop["name"], shop["location"],
                          shop["products"]) for shop in shopping_dict["shops"]]

        for index, customer in enumerate(customer_list):
            # make a Customer instance
            person = Customer(customer["name"], customer["money"],
                              customer["product_cart"], customer["location"])
            print(person)

            # make a Car instance
            car = Car(customer["car"]["fuel_consumption"])

            # calculating cost for each shop
            min_cost = float("inf")
            cheapest_store = ""
            selected_trip_cost = 0.0
            for shop in shop_list:
                distance_to_store = shop.calculate_distance(person.location)
                fuel_cost = car.cost_to_drive(distance_to_store, fuel_price)
                total_product_cost = shop.calculate_total_price(
                    person.list_of_products())
                shopping_trip_cost = round(
                    ((fuel_cost * 2) + total_product_cost), 2)
                print(f"{person.name}'s trip to the {shop.name} "
                      f"costs {shopping_trip_cost}")
                if shopping_trip_cost < min_cost:
                    cheapest_store = shop
                    min_cost = shopping_trip_cost
                    selected_trip_cost = shopping_trip_cost

            # drive to cheapest shop if possible
            if person.money >= min_cost:
                print(f"{person.name} rides to {cheapest_store.name}")
                person.location = cheapest_store.location
                time = datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
                print()
                print(f"Date: {time}")
                cheapest_store.print_purchased_products(person)
                remaining_money = person.money - selected_trip_cost
                print(f"{person.name} now has {remaining_money} dollars")
                if index < len(customer_list) - 1:
                    print()
            else:
                print(f"{person.name} doesn't have enough money "
                      f"to make a purchase in any shop")
                if index < len(customer_list) - 1:
                    print()
