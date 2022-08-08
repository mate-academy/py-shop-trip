import datetime
import json

from app.calc_dist import dist_from_customer, calculate_cost_of_ride

from app.calc_purchases import \
    calc_purchases,\
    shop_products,\
    print_bought_products


def shop_trip():
    with open("app/config.json", "r") as file:
        config = json.load(file)
        fuel_price = config["FUEL_PRICE"]
        customers = config["customers"]
        shops = config["shops"]

    for customer in customers:
        print(f"{customer['name']} has {customer['money']} dollars")
        result = {}
        for shop in shops:
            distance = dist_from_customer(
                customer["location"][0],
                customer["location"][1],
                shop["location"][0],
                shop["location"][1])

            ride_cost = calculate_cost_of_ride(
                customer["car"]["fuel_consumption"],
                distance,
                fuel_price)

            sum_of_products = calc_purchases(
                customer["product_cart"],
                shop["products"])

            cost_of_trip = ride_cost * 2 + sum_of_products
            cost_of_trip = round(cost_of_trip, 2)
            result[shop["name"]] = cost_of_trip
            print(
                f"{customer['name']}'s "
                f"trip to the {shop['name']} costs {cost_of_trip}")

        ls_with_values_of_each_trip = sorted(list(result.values()))

        ls_with_name_of_cheapest_trp_shop = \
            [k for k, v in result.items()
             if v == ls_with_values_of_each_trip[0]]

        if ls_with_values_of_each_trip[0] <= customer["money"]:
            print(f"{customer['name']} "
                  f"rides to {ls_with_name_of_cheapest_trp_shop[0]}\n")

            now = datetime.datetime.now()
            date_to_print = now.strftime("%d/%m/%Y %H:%M:%S")

            print(f"Date: {date_to_print}")
            print(f"Thanks, {customer['name']}, for you purchase!")

            dict_of_products =\
                shop_products(shops, ls_with_name_of_cheapest_trp_shop[0])
            print_bought_products(customer["product_cart"], dict_of_products)

            print(f"{customer['name']} rides home")
            rest_of_money = customer["money"] - ls_with_values_of_each_trip[0]
            print(f"{customer['name']} now has {rest_of_money} dollars\n")
        else:
            print(f"{customer['name']} "
                  f"doesn't have enough money to make purchase in any shop")
