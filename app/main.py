import json

from app.customer import Customer

from app.car import Car

from app.shop import Shop


def shop_trip() -> None:
    with (open("app/config.json") as file):
        python_dict = json.load(file)
        for customer in python_dict["customers"]:
            print(f'{customer["name"]} has {customer["money"]} dollars')
            trip_dict = {}
            for shop in python_dict["shops"]:
                cost_trip = round(Car.calculate_fuel_cost(
                    fuel_consumption=customer["car"]["fuel_consumption"],
                    distance=Customer.calculate_distance(
                        location1=customer["location"],
                        location2=shop["location"]
                    ),
                    fuel_price=python_dict["FUEL_PRICE"]
                ) * 2 + Shop.cost_all_products(
                    products=shop["products"],
                    product_cart=customer["product_cart"]
                ), 2)
                shop["cost_trip"] = cost_trip
                print(f"{customer['name']}'s"
                      f" trip to the {shop['name']} costs {cost_trip}")
                trip_dict[shop["name"]] = cost_trip
            key_min_value = min(trip_dict, key=lambda k: trip_dict[k])
            if customer["money"] < trip_dict[key_min_value]:
                print(
                    f"{customer['name']} "
                    f"doesn't have enough money to make a purchase in any shop"
                )
                break
            print(f"{customer['name']} rides to {key_min_value}\n")
            print("Date: 04/01/2021 12:33:41")
            print(f"Thanks, {customer['name']}, for your purchase!")
            print("You have bought:")
            sum_all_product = 0
            for shop in python_dict["shops"]:
                if shop["name"] == key_min_value:
                    for i in shop["products"]:
                        sum_product = round(
                            customer["product_cart"][i] * shop["products"][i],
                            2)
                        if float(sum_product) == int(sum_product):
                            sum_product = int(sum_product)
                        print(f"{customer['product_cart'][i]} {i}s for "
                              f"{sum_product} dollars")
                        sum_all_product += sum_product
                    rest_money = round(
                        customer["money"] - shop["cost_trip"], 2)
            print(f"Total cost is {sum_all_product} dollars")
            print("See you again!\n")
            print(f"{customer['name']} rides home")
            print(f"{customer['name']} now has {rest_money} dollars\n")
