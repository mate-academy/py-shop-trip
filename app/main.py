import datetime
import json
from app.car import cost_of_road
from app.customer import make_customer_from_json_file
from app.shop import create_shops, distance


def shop_trip() -> None:
    with open("app/config.json", "r") as file:
        file_read = json.load(file)

    customers = make_customer_from_json_file(file_read)
    shops = create_shops(file_read)

    for customer in customers:

        length_of_roads = []
        saved_location = customer.location

        for shop in shops:
            length_road = distance(shop.location, customer.location)
            length_of_roads.append([shop.name, length_road])

        costs_for_each_shop = {}
        for name_product, value_product in customer.product_carts.items():
            for shop in shops:
                if shop.name not in costs_for_each_shop:
                    costs_for_each_shop[shop.name] = {}
                dictionary = {
                    name_product:
                        shop.products[name_product] * value_product
                }
                costs_for_each_shop[shop.name].update(dictionary)
                shop_location = shop.location

        print(f"{customer.name} has {customer.money} dollars")
        all_costs = []
        for _distance in length_of_roads:
            cost_both_roads = (
                2 * cost_of_road(
                    customer.used_fuel_in_dollars, _distance[1]
                )
            )
            for shop, dict_value in costs_for_each_shop.items():
                if shop == _distance[0]:
                    total_shop_costs = (
                        sum(value for value in dict_value.values()))
                    total_costs = round(total_shop_costs + cost_both_roads, 2)
                    print(
                        f"{customer.name}'s trip to the"
                        f" {shop} costs{total_costs: .2f}"
                    )
                    all_costs.append(
                        [
                            shop, total_shop_costs + cost_both_roads
                        ]
                    )
        shops_costs = sorted(all_costs, key=lambda x: x[1])
        shop_for_customer = shops_costs[0][0]

        products_price = {}

        for name_product, value_product in customer.product_carts.items():
            products_price[name_product] = 0
            for shop in shops:
                if shop.name == shop_for_customer:
                    products_price[name_product] += (
                        shop.products[name_product] * value_product
                    )
                    shop_location = shop.location

        values = []
        for shop in all_costs:
            if shop[0] == shop_for_customer:
                go_shop_for_customer_cost = shop[1]
            values.append(shop[1])
        if all(value > customer.money for value in values):
            print(
                f"{customer.name} doesn't have enough money "
                f"to make a purchase in any shop"
            )
            continue
        else:
            print(f"{customer.name} rides to {shop_for_customer}\n")
            customer.location = shop_location
            current_date = (
                datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")
            )
            print(f"Date: {current_date}")
            print(f"Thanks, {customer.name}, for your purchase!")
            print("You have bought:")
            for product, value in products_price.items():
                display_value = int(value) if value == int(value) else value
                print(f"{customer.product_carts[product]} "
                      f"{product}s for {display_value} dollars")
            print(f"Total cost is {sum(products_price.values())} dollars")
            print("See you again!\n")
            print(f"{customer.name} rides home")
            print(f"{customer.name} "
                  f"now has"
                  f"{(customer.money - go_shop_for_customer_cost): .2f}"
                  f" dollars\n"
                  )
            customer.location = saved_location
