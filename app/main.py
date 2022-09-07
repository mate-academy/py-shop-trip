import json
import datetime


def shop_trip():
    with open("app/config.json") as file:
        file_data = json.load(file)
    fuel_price = file_data["FUEL_PRICE"]
    res_dict = {}
    shop_price_list = {}
    for user in file_data["customers"]:
        name = user["name"]
        res_dict[name] = {}

        for shop in file_data["shops"]:
            calc_trip_cost = calc_cost_trip(user, shop, fuel_price)
            shop_name = shop["name"]
            res_dict[name][shop_name] = calc_trip_cost

        shop_min_cost = min(res_dict[name], key=res_dict[name].get)

        for shop in file_data["shops"]:
            if shop["name"] == shop_min_cost:
                shop_price_list = shop["products"]

        go_to_shop(shop_price_list, user, shop_min_cost, res_dict)
        res_dict.clear()


def calc_cost_trip(user, shop, fuel_price):
    x_diff = user["location"][0] - shop["location"][0]
    y_diff = user["location"][1] - shop["location"][1]
    distance = ((x_diff ** 2) + (y_diff ** 2)) ** 0.5
    shop_location = shop["location"]
    fuel_consumption = user["car"]["fuel_consumption"]
    travel_cost = distance * fuel_price * fuel_consumption / 100 * 2
    product_cost = sum(
        [
            shop['products'][key] * value
            for key, value in user["product_cart"].items()
        ]
    )
    total_cost = round(product_cost + travel_cost, 2)
    return [total_cost, shop_location]


def go_to_shop(shop_price_list, user, shop, res):
    shop_location = []
    home_location = user["location"]
    money = user["money"]
    total_check = 0
    total_cost = 0
    print(f"{user['name']} has {money} dollars")
    for value in res.values():
        for key, val in value.items():
            if key == shop:
                shop_location = val[1]
                total_cost = val[0]
            print(f"{user['name']}'s trip to the {key} costs {val[0]}")
    if money < total_cost:
        print(f"{user['name']} doesn't have enough money"
              f" to make purchase in any shop")
    else:
        print(f"{user['name']} rides to {shop}\n")
        user["location"] = shop_location
        print(f'Date: {datetime.datetime.now().strftime("%d/%m/%Y %H:%M:%S")}')
        print(f"Thanks, {user['name']}, for you purchase!")
        print("You have bought: ")
        for product, count in user["product_cart"].items():
            price = count * shop_price_list[product]
            total_check += price
            print(f"{count} {product}s for {price} dollars")
        print(f"Total cost is {total_check} dollars")
        print("See you again!\n")
        print(f"{user['name']} rides home")
        user["location"] = home_location
        print(f"{user['name']} now has {money - total_cost} dollars\n")
