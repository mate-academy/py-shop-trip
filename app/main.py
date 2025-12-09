import json

from app.customer import Customer
from app.shop import Shop
from app.car import Car


def shop_trip() -> None:
    with open("app/config.json", "r") as json_file:
        trip_data = json.load(json_file)

    fuel_price = trip_data["FUEL_PRICE"]
    customers = []
    shops = []
    for person in trip_data["customers"]:
        car_obj = Car(
            person["car"]["brand"],
            person["car"]["fuel_consumption"]
        )
        customer = Customer(
            person["name"],
            person["product_cart"],
            person["location"],
            person["money"],
            car_obj
        )
        customers.append(customer)
    for place in trip_data["shops"]:
        shop = Shop(
            place["name"],
            place["location"],
            place["products"]
        )
        shops.append(shop)

    for customer in customers:
        customer.money_status()

        suitable_shops = []
        for shop in shops:
            if customer.has_all_products(shop):
                distance_one_way = customer.count_distance(shop)
                distance_round_way = distance_one_way * 2

                products_cost = customer.calculate_products_cost(shop)
                fuel_cost = customer.calculate_fuel_cost(
                    distance_round_way,
                    fuel_price
                )
                total_cost = products_cost + fuel_cost

                print(f"{customer.name}'s trip to "
                      f"the {shop.name} costs {total_cost:.2f}")
                suitable_shops.append((shop, total_cost, products_cost))

        if suitable_shops:
            cheapest_shop, cheapest_cost, products_cost = min(
                suitable_shops,
                key=lambda x: x[1]
            )

            if customer.money >= cheapest_cost:
                customer.ride_to_shop(cheapest_shop)
                cheapest_shop.give_receipt(customer, products_cost)
                customer.ride_home()
                customer.spend_money(cheapest_cost)
                print(f"{customer.name} now "
                      f"has {customer.money:.2f} dollars")
            else:
                print(f"{customer.name} doesn't have "
                      f"enough money to make a purchase in any shop")
        else:
            print(f"{customer.name} cannot find all "
                  f"needed products in any shop")

        if customer != customers[-1]:
            print()
