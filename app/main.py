import json


def calculate_distance(coord1: list, coord2: list):
    distance = ((coord1[0] - coord2[0]) ** 2 + (coord1[1] - coord2[1]) ** 2)
    return distance ** 0.5


def shop_trip():
    config_json_content = {}
    with open("app/config.json")as file:
        data = json.load(file)
        config_json_content.update(data)

    fuel_price = config_json_content["FUEL_PRICE"]
    shops = []
    customers = []

    customers += (config_json_content["customers"])
    shops += (config_json_content["shops"])

    shop_list_each_name_each_store = []

    for name in range(len(customers)):
        sum_for_name_for_each_store = []
        for shop in range(len(shops)):
            price = 0
            products = ["milk", "bread", "butter"]
            for product in products:
                price += customers[name]["product_cart"][product] * \
                    shops[shop]["products"][product]
            dist = calculate_distance(customers[name]["location"],
                                      shops[shop]["location"])
            car_eats = customers[name]["car"]["fuel_consumption"]
            fuel = fuel_price * dist * car_eats * 2 / 100
            price += fuel
            sum_for_name_for_each_store.append(round(price, 2))
        shop_list_each_name_each_store.append(sum_for_name_for_each_store)

    for person in range(len(customers)):
        budget = customers[person]["money"]
        food = customers[person]['product_cart']
        name = customers[person]['name']
        print(f"{name} "
              f"has {customers[person]['money']} dollars")
        print(f"{name}'s trip to the Outskirts Shop "
              f"costs {shop_list_each_name_each_store[person][0]}")
        print(f"{name}'s trip to the Shop '24/7' "
              f"costs {shop_list_each_name_each_store[person][1]}")
        print(f"{name}'s trip to the Central Shop "
              f"costs {shop_list_each_name_each_store[person][2]}")
        if budget < \
                min(shop_list_each_name_each_store[person]):
            print(f"{name} doesn\'t "
                  f"have enough money to make purchase in any shop")
        else:
            if min(shop_list_each_name_each_store[person]) == \
                    shop_list_each_name_each_store[person][0]:
                shop_id = 0
                print(f"{name} rides to Outskirts Shop")
            elif min(shop_list_each_name_each_store[person]) == \
                    shop_list_each_name_each_store[person][1]:
                shop_id = 1
                print(f"{name} rides to Shop \'24/7\'")
            elif min(shop_list_each_name_each_store[person]) == \
                    shop_list_each_name_each_store[person][2]:
                shop_id = 2
                print(f"{name} rides to Central Shop")
            print("\nDate: 11/03/2020 13:15:34")

            milk_price = customers[person]["product_cart"]["milk"] * \
                shops[shop_id]["products"]["milk"]
            bread_price = customers[person]["product_cart"]["bread"] * \
                shops[shop_id]["products"]["bread"]
            butter_price = customers[person]["product_cart"]["butter"] * \
                shops[shop_id]["products"]["butter"]
            total_cost = milk_price + bread_price + butter_price

            market = shops[shop_id]["location"]
            home = customers[person]["location"]
            x_coord_square = (home[0] - market[0]) ** 2
            y_coord_square = (home[1] - market[1]) ** 2
            distance = (x_coord_square + y_coord_square) ** 0.5
            car_drinks = customers[person]["car"]["fuel_consumption"]
            fuel_cost = fuel_price * distance * car_drinks * 2 / 100
            money_left = round(budget - total_cost - fuel_cost, 2)

            print(f"Thanks, {name}, for you purchase!")
            print(f"You have bought: \n"
                  f"{food['milk']} milks for {milk_price} dollars\n"
                  f"{food['bread']} breads for {bread_price} dollars\n"
                  f"{food['butter']} butters for {butter_price} dollars")
            print(f"Total cost is {total_cost} dollars")
            print("See you again!\n")
            print(f"{name} rides home")
            print(f"{name} now has {money_left} dollars\n")
