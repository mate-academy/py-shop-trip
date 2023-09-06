import json
import math
import datetime


def shop_trip():
    with open("app/config.json", "r") as data_file:
        data = json.load(data_file)

    customers = data["customers"]
    shops = data["shops"]
    fuel_price: float = data["FUEL_PRICE"]

    for customer in customers:
        dict_price_products = {}
        cost_trip_to_shop = {}
        print(f"{customer['name']} has {customer['money']} dollars")

        for shop in shops:
            dict_price_products.update({shop["name"]: {}})
            price_of_products = 0
            dist_shop = math.dist(customer["location"], shop["location"]) * 2
            fuel_consumption = customer["car"]["fuel_consumption"]
            trip_price = round(
                dist_shop * fuel_consumption / 100 * fuel_price, 2
            )

            for product in customer["product_cart"].keys():
                quantity_product = customer["product_cart"][product]
                price_of_product = shop["products"][product] * quantity_product
                price_of_products += price_of_product
                dict_price_products[shop["name"]].update(
                    {f"{customer['product_cart'][product]} {product}"
                     : price_of_product}
                )

            dict_price_products[shop["name"]].update(
                {"all_price": price_of_products}
            )
            costs = dict_price_products[shop["name"]]["all_price"] + trip_price
            cost_trip_to_shop[shop["name"]] = costs
            print(f"{customer['name']}'s trip "
                  f"to the {shop['name']} costs {costs}")

        shop_to_trip = min(cost_trip_to_shop, key=cost_trip_to_shop.get)

        if customer["money"] < costs:
            print(f"{customer['name']} doesn't have "
                  f"enough money to make purchase in any shop")
        else:
            remnant_cash = customer['money'] - cost_trip_to_shop[shop_to_trip]
            now_date = datetime.datetime.now().strftime('%d/%m/%Y %H:%M:%S')

            print(f"{customer['name']} rides to {shop_to_trip}\n")
            print(f"Date: {now_date}")
            print(f"Thanks, {customer['name']}, for you purchase!")
            print("You have bought: ")
            for product, price in dict_price_products[shop_to_trip].items():
                if product != "all_price":
                    print(f"{product}s for {price} dollars")

            print(f"Total cost is"
                  f" {dict_price_products[shop_to_trip]['all_price']} dollars")
            print("See you again!\n")
            print(f"{customer['name']} rides home")
            print(f"{customer['name']} now has {remnant_cash} dollars\n")
